from geoalchemy2.elements import WKTElement
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.emergency_request import EmergencyRequest
from app.repositories.emergency_notification_repository import (EmergencyNotificationRepository,)
from app.repositories.emergency_request_repository import (EmergencyRequestRepository,)
from app.repositories.spatial_repository import SpatialRepository
from uuid import UUID
from fastapi import HTTPException

class EmergencyRequestService:
    @staticmethod
    async def create_sos(
        db: AsyncSession,
        data,
        requester_id=None,
    ):
        # Create PostGIS geography point
        point = WKTElement(
            f"POINT({data.longitude} {data.latitude})",
            srid=4326,
        )

        emergency = EmergencyRequest(
            category_id=data.category_id,
            requester_id=requester_id,
            description=data.description,
            location=point,
        )
        await EmergencyRequestRepository.create(db, emergency)

        # Find nearest volunteers
        nearby_volunteers = await SpatialRepository.nearest_volunteers(
            db,
            latitude=data.latitude,
            longitude=data.longitude,
            limit=20,
        )

        # First batch = nearest 3 volunteers
        first_batch = nearby_volunteers[:3]

        await EmergencyNotificationRepository.create_batch(
            db=db,
            emergency_request_id=emergency.id,
            volunteers=first_batch,
            batch_number=1,
        )

        # Find rescue contacts
        nearest_rescue  = await SpatialRepository.nearest_rescue_contacts(
            db,
            latitude=data.latitude,
            longitude=data.longitude,
            limit=1,
        )
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
        medical_facilities = await SpatialRepository.nearest_facilities(
            db,
            latitude=data.latitude,
            longitude=data.longitude,
            limit=5,
        )
        await db.commit()

        return {
            "emergency_id": str(emergency.id),
            "notified_volunteers": len(first_batch),
            "nearest_rescue_contact": nearest_rescue_contact,
            "medical_facilities": medical_facilities,
        }
        
    @staticmethod
    async def accept_emergency(
        db: AsyncSession,
        emergency_id: UUID,
        volunteer_id: UUID,
    ):

        emergency = await EmergencyRequestRepository.get_by_id(db, emergency_id)

        if emergency is None:
            raise HTTPException(404, "Emergency request not found")

        notification = await EmergencyNotificationRepository.get_for_volunteer(
            db,
            emergency_id,
            volunteer_id,
        )

        if notification is None:
            raise HTTPException(403, "You were not notified for this emergency")

        if emergency.assigned_volunteer_id is not None:
            raise HTTPException(409, "Emergency already assigned")

        await EmergencyNotificationRepository.mark_accepted(db, notification)

        await EmergencyNotificationRepository.cancel_other_pending(
            db,
            emergency_id,
            volunteer_id,
        )

        await EmergencyRequestRepository.assign_volunteer(
            db,
            emergency,
            volunteer_id,
        )

        await db.commit()

        return {
            "emergency_id": emergency.id,
            "volunteer_id": volunteer_id,
            "status": emergency.status.value,
            "message": "Emergency accepted successfully",
        }
        
        