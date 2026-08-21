from uuid import UUID
from fastapi import HTTPException
from geoalchemy2.elements import WKTElement
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.models.emergency_request import EmergencyRequest
from app.repositories.emergency_notification_repository import EmergencyNotificationRepository
from app.repositories.emergency_request_repository import EmergencyRequestRepository
from app.repositories.spatial_repository import SpatialRepository
from app.repositories.device_token_repository import DeviceTokenRepository
from app.repositories.emergency_category_repository import EmergencyCategoryRepository
from app.services.fcm_service import FCMService

class EmergencyRequestService:
    @staticmethod
    async def create_sos(db: AsyncSession, data, requester_id=None):
        # Create PostGIS geography point
        point = WKTElement(f"POINT({data.longitude} {data.latitude})", srid=4326)
        emergency = EmergencyRequest(
            category_id=data.category_id,
            requester_id=requester_id,
            description=data.description,
            location=point,
        )
        await EmergencyRequestRepository.create(db, emergency)

        # Find nearest volunteers
        nearby_volunteers = await SpatialRepository.nearest_volunteers(db, latitude=data.latitude, longitude=data.longitude, limit=20)
        first_batch = nearby_volunteers[:3]

        await EmergencyNotificationRepository.create_batch(db=db, emergency_request_id=emergency.id, volunteers=first_batch, batch_number=1)

        category = await EmergencyCategoryRepository.get_by_id(db, data.category_id)
        if category is None:
            raise HTTPException(404, "Emergency category not found")

        # Find rescue contacts
        nearest_rescue = await SpatialRepository.nearest_rescue_contacts(db, latitude=data.latitude, longitude=data.longitude, limit=1)
        if not nearest_rescue:
            nearest_rescue_contact = {
                "id": "fallback",
                "name_en": "Myanmar Emergency Ambulance",
                "phone": "192",
                "type": "AMBULANCE",
                "latitude": 0.0,
                "longitude": 0.0,
                "distance_meters": 0.0,
            }
        else:
            nearest_rescue_contact = nearest_rescue[0]

        # Find medical facilities
        medical_facilities = await SpatialRepository.nearest_facilities(db, latitude=data.latitude, longitude=data.longitude, limit=5)
        await db.commit()

        for volunteer in first_batch:
            device_tokens = await DeviceTokenRepository.get_tokens_for_volunteer(db, volunteer["volunteer_id"])
            for token in device_tokens:
                await FCMService.send_emergency_notification(
                    token=token,
                    emergency_id=str(emergency.id),
                    category_name=category.name_en,
                    distance_meters=float(volunteer["distance_meters"]),
                )

        return {
            "emergency_id": emergency.id,
            "notified_volunteers": len(first_batch),
            "nearest_rescue_contact": nearest_rescue_contact,
            "medical_facilities": medical_facilities,
        }

    @staticmethod
    async def accept_emergency(db: AsyncSession, emergency_id: UUID, volunteer_id: UUID):
        emergency = await EmergencyRequestRepository.get_by_id(db, emergency_id)
        if emergency is None:
            raise HTTPException(404, "Emergency request not found")

        notification = await EmergencyNotificationRepository.get_for_volunteer(db, emergency_id, volunteer_id)
        if notification is None:
            raise HTTPException(403, "You were not notified for this emergency")

        if emergency.assigned_volunteer_id is not None:
            raise HTTPException(409, "Emergency already assigned")

        await EmergencyNotificationRepository.mark_accepted(db, notification)
        await EmergencyNotificationRepository.cancel_other_pending(db, emergency_id, volunteer_id)
        await EmergencyRequestRepository.assign_volunteer(db, emergency, volunteer_id)
        await db.commit()

        return {
            "emergency_id": emergency.id,
            "volunteer_id": volunteer_id,
            "status": emergency.status.value,
            "message": "Emergency accepted successfully",
        }

    @staticmethod
    async def get_emergency_status(db: AsyncSession, emergency_id: UUID):
        result = await EmergencyRequestRepository.get_status_with_volunteer(db, emergency_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Emergency request not found")

        (emergency, volunteer_latitude, volunteer_longitude, volunteer_speed, volunteer_heading, distance_meters) = result

        # Emergency location
        location_result = await db.execute(
            text("SELECT ST_Y(location::geometry) AS latitude, ST_X(location::geometry) AS longitude FROM emergency_requests WHERE id = :emergency_id"),
            {"emergency_id": emergency.id},
        )
        location = location_result.mappings().first()

        assigned_volunteer = None
        if emergency.assigned_volunteer is not None and emergency.assigned_volunteer.user is not None:
            current_location = None
            if volunteer_latitude is not None and volunteer_longitude is not None:
                current_location = {
                    "latitude": float(volunteer_latitude),
                    "longitude": float(volunteer_longitude),
                    "speed": float(volunteer_speed) if volunteer_speed is not None else None,
                    "heading": float(volunteer_heading) if volunteer_heading is not None else None,
                }

            assigned_volunteer = {
                "id": str(emergency.assigned_volunteer.id),
                "name": emergency.assigned_volunteer.user.full_name,
                "phone": emergency.assigned_volunteer.user.phone,
                "location": current_location,
            }

        return {
            "emergency_id": emergency.id,
            "status": emergency.status.value,
            "category_id": emergency.category.id,
            "category_name_en": emergency.category.name_en,
            "category_name_mm": emergency.category.name_mm,
            "description": emergency.description,
            "latitude": float(location["latitude"]) if location else 0.0,
            "longitude": float(location["longitude"]) if location else 0.0,
            "distance_meters": float(distance_meters) if distance_meters is not None else None,
            "assigned_volunteer": assigned_volunteer,
        }