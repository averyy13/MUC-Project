from uuid import UUID
from fastapi import HTTPException, status
from geoalchemy2.elements import WKTElement
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.models.emergency_request import EmergencyRequest
from app.models.enums import AssignmentStatus, EmergencyStatus
from app.repositories.emergency_notification_repository import EmergencyNotificationRepository
from app.repositories.emergency_request_repository import EmergencyRequestRepository
from app.repositories.spatial_repository import SpatialRepository
from app.repositories.device_token_repository import DeviceTokenRepository
from app.repositories.emergency_category_repository import EmergencyCategoryRepository
from app.repositories.volunteer_repository import VolunteerRepository
from app.repositories.volunteer_assignment_repository import VolunteerAssignmentRepository
from app.services.fcm_service import FCMService
from app.services.google_routes_service import GoogleRoutesService
from app import db

class EmergencyRequestService:

    @staticmethod
    async def create_sos(db: AsyncSession, data, requester_id=None):
        point = WKTElement(f"POINT({data.longitude} {data.latitude})", srid=4326)
        emergency = EmergencyRequest(
            category_id=data.category_id, requester_id=requester_id, 
            description=data.description, location=point
        )
        await EmergencyRequestRepository.create(db, emergency)

        nearby_volunteers = await SpatialRepository.nearest_volunteers(
            db, latitude=data.latitude, longitude=data.longitude, limit=20
        )
        first_batch = nearby_volunteers[:3]

        await EmergencyNotificationRepository.create_batch(
            db=db, emergency_request_id=emergency.id, volunteers=first_batch, batch_number=1
        )
        for volunteer in first_batch:
            await VolunteerAssignmentRepository.create(
                db=db,request_id=emergency.id,volunteer_id=volunteer["volunteer_id"],notification_round=1,
            )
        category = await EmergencyCategoryRepository.get_by_id(db, data.category_id)
        if category is None:
            raise HTTPException(404, "Emergency category not found")

        nearest_rescue = await SpatialRepository.nearest_rescue_contacts(
            db, latitude=data.latitude, longitude=data.longitude, limit=1
        )
        if not nearest_rescue:
            nearest_rescue_contact = {
                "id": "fallback", "name_en": "Myanmar Emergency Ambulance",
                "phone": "192", "type": "AMBULANCE", "latitude": 0.0,
                "longitude": 0.0, "distance_meters": 0.0,
            }
        else:
            nearest_rescue_contact = nearest_rescue[0]

        medical_facilities = await SpatialRepository.nearest_facilities(
            db, latitude=data.latitude, longitude=data.longitude, limit=5
        )
        await db.commit()

        for volunteer in first_batch:
            device_tokens = await DeviceTokenRepository.get_tokens_for_volunteer(db, volunteer["volunteer_id"])
            for token in device_tokens:
                await FCMService.send_emergency_notification(
                    token=token, emergency_id=str(emergency.id),
                    category_name=category.name_en, distance_meters=float(volunteer["distance_meters"])
                )

        return {
            "emergency_id": emergency.id,
            "notified_volunteers": len(first_batch),
            "nearest_rescue_contact": nearest_rescue_contact,
            "medical_facilities": medical_facilities,
        }

    @staticmethod
    async def accept_emergency(db: AsyncSession, emergency_id: UUID, user_id: UUID):
        volunteer = await VolunteerRepository.get_by_user_id(db,user_id)
        if volunteer is None:
            raise HTTPException(status_code=404, detail="Volunteer not found")
        volunteer_id = volunteer.id
        emergency = await EmergencyRequestRepository.get_by_id(db, emergency_id)
        if emergency is None:
            raise HTTPException(status_code=404, detail="Emergency request not found")

        notification = await EmergencyNotificationRepository.get_for_volunteer(db, emergency_id, volunteer_id)
        if notification is None:
            raise HTTPException(status_code=403, detail="You were not notified for this emergency")

        if emergency.assigned_volunteer_id is not None:
            raise HTTPException(status_code=409, detail="Emergency already assigned")

        assignment = await VolunteerAssignmentRepository.get_for_request_and_volunteer(db, emergency_id, volunteer_id)
        if assignment is None:
            raise HTTPException(status_code=404, detail="Volunteer assignment not found")

        if assignment.status != AssignmentStatus.PENDING:
            raise HTTPException(status_code=409, detail=f"Assignment is already {assignment.status.value}")

        await VolunteerAssignmentRepository.accept(db, assignment)
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
        (emergency, vol_lat, vol_lon, vol_speed, vol_heading, distance_meters) = result

        location_result = await db.execute(
            text("SELECT ST_Y(location::geometry) AS latitude, ST_X(location::geometry) AS longitude FROM emergency_requests WHERE id = :emergency_id"),
            {"emergency_id": emergency.id},
        )
        location = location_result.mappings().first()

        assignment = None
        if emergency.assigned_volunteer_id is not None:
            assignment = await VolunteerAssignmentRepository.get_for_request_and_volunteer(
                db, emergency.id, emergency.assigned_volunteer_id
            )
            
        assigned_volunteer = None
        if emergency.assigned_volunteer is not None and emergency.assigned_volunteer.user is not None:
            current_location = None
            if vol_lat is not None and vol_lon is not None:
                current_location = {
                    "latitude": float(vol_lat),
                    "longitude": float(vol_lon),
                    "speed": float(vol_speed) if vol_speed is not None else None,
                    "heading": float(vol_heading) if vol_heading is not None else None,
                }
            assigned_volunteer = {
                "id": str(emergency.assigned_volunteer.id),
                "name": emergency.assigned_volunteer.user.full_name,
                "phone": emergency.assigned_volunteer.user.phone,
                "location": current_location,
            }
            
        assignment_status = assignment.status.value if assignment is not None else None
        
        return {
            "emergency_id": emergency.id,
            "status": emergency.status.value,
            "assignment_status": assignment_status,
            "category_id": emergency.category.id,
            "category_name_en": emergency.category.name_en,
            "category_name_mm": emergency.category.name_mm,
            "description": emergency.description,
            "latitude": float(location["latitude"]) if location else 0.0,
            "longitude": float(location["longitude"]) if location else 0.0,
            "distance_meters": float(distance_meters) if distance_meters is not None else None,
            "assigned_volunteer": assigned_volunteer,
        }
        
    @staticmethod
    async def start_rescue(db: AsyncSession, emergency_id: UUID, user_id):
        volunteer = await VolunteerRepository.get_by_user_id(db, user_id)
        if volunteer is None:
            raise HTTPException(status_code=404, detail="Volunteer not found")
    
        emergency = await EmergencyRequestRepository.get_by_id(db, emergency_id)
        if emergency is None:
            raise HTTPException(status_code=404, detail="Emergency request not found")
            
        assignment = await VolunteerAssignmentRepository.get_for_request_and_volunteer(
            db, emergency.id, volunteer.id
        )
        if assignment is None:
            raise HTTPException(status_code=404, detail="Volunteer assignment not found")
        if assignment.status != AssignmentStatus.ACCEPTED:
            raise HTTPException(status_code=409, detail="Volunteer assignment is not accepted")
    
        await EmergencyRequestRepository.start_rescue(db=db, emergency=emergency, volunteer_id=volunteer.id)
        
        await db.commit()
    
        return {
            "emergency_id": emergency.id,
            "volunteer_id": volunteer.id,
            "status": emergency.status.value,
            "assignment_status": assignment.status.value,
            "message": "Volunteer is now en route.",
        }
        
    @staticmethod
    async def get_emergency_route(db: AsyncSession, emergency_id):
        requester_location = await EmergencyRequestRepository.get_location(db, emergency_id)
        if requester_location is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Emergency request not found.")

        volunteer_id = await EmergencyRequestRepository.get_assigned_volunteer_id(db, emergency_id)
        if volunteer_id is None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="No volunteer has been assigned to this emergency.")

        volunteer_location = await VolunteerRepository.get_current_location(db, volunteer_id)
        if volunteer_location is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Volunteer current location not found.")
       
        route = await GoogleRoutesService.compute_route(
            origin_latitude=float(volunteer_location["latitude"]),
            origin_longitude=float(volunteer_location["longitude"]),
            destination_latitude=float(requester_location["latitude"]),
            destination_longitude=float(requester_location["longitude"]),
        )

        return {
            "emergency_id": str(emergency_id),
            "volunteer_latitude": float(volunteer_location["latitude"]),
            "volunteer_longitude": float(volunteer_location["longitude"]),
            "requester_latitude": float(requester_location["latitude"]),
            "requester_longitude": float(requester_location["longitude"]),
            "distance_meters": route["distance_meters"],
            "duration_seconds": route["duration_seconds"],
            "encoded_polyline": route["encoded_polyline"],
        }
        
    @staticmethod
    async def mark_arrived(db: AsyncSession, emergency_id: UUID, user_id):
        volunteer = await VolunteerRepository.get_by_user_id(db, user_id)
        if volunteer is None:
            raise HTTPException(status_code=404, detail="Volunteer not found")
    
        emergency = await EmergencyRequestRepository.get_by_id(db, emergency_id)
        if emergency is None:
            raise HTTPException(status_code=404, detail="Emergency request not found")
        if emergency.status != EmergencyStatus.VOLUNTEER_EN_ROUTE:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "Volunteer cannot mark arrived while "
                    f"emergency status is {emergency.status.value}."
                ),
            )
        assignment = await VolunteerAssignmentRepository.get_for_request_and_volunteer(
            db, emergency.id, volunteer.id
        )
        if assignment is None:
            raise HTTPException(status_code=404, detail="Volunteer assignment not found")
        if assignment.status != AssignmentStatus.ACCEPTED:
            raise HTTPException(status_code=409, detail="Volunteer assignment is "
                f"{assignment.status.value}, not ACCEPTED.")

        await VolunteerAssignmentRepository.mark_arrived(db, assignment)
        # await EmergencyRequestRepository.mark_arrived(db=db,emergency=emergency,volunteer_id=volunteer.id)
        await db.commit()
    
        return {
            "emergency_id": emergency.id,
            "volunteer_id": volunteer.id,
            "status": emergency.status.value,
            "assignment_status": assignment.status.value,
            "message": "Volunteer has arrived.",
        }
        
    @staticmethod
    async def complete_rescue(db: AsyncSession, emergency_id: UUID, user_id):
        volunteer = await VolunteerRepository.get_by_user_id(db, user_id)
        if volunteer is None:
            raise HTTPException(status_code=404, detail="Volunteer not found")

        emergency = await EmergencyRequestRepository.get_by_id(db, emergency_id)
        if emergency is None:
            raise HTTPException(status_code=404, detail="Emergency request not found")
        if emergency is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Emergency request not found",)

        if emergency.status != EmergencyStatus.VOLUNTEER_EN_ROUTE:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    "Emergency cannot be completed while "
                    f"status is {emergency.status.value}."
                ),
            )

        assignment = await VolunteerAssignmentRepository.get_for_request_and_volunteer(
            db, emergency.id, volunteer.id
        )
        if assignment is None:
            raise HTTPException(status_code=404, detail="Volunteer assignment not found")
        if assignment.status != AssignmentStatus.ARRIVED:
            raise HTTPException(status_code=409, detail="Volunteer must arrive before completing rescue")
     
        await VolunteerAssignmentRepository.complete(db, assignment)
        emergency.status = EmergencyStatus.COMPLETED
        # await EmergencyRequestRepository.complete_rescue(db=db,emergency=emergency,volunteer_id=volunteer.id)
        await db.commit()

        return {
            "emergency_id": emergency.id,
            "volunteer_id": volunteer.id,
            "status": emergency.status.value,
            "assignment_status": assignment.status.value,
            "message": "Rescue completed successfully.",
        }   
    
    @staticmethod
    async def get_active_emergency_for_volunteer(db: AsyncSession, user_id):
        volunteer = await VolunteerRepository.get_by_user_id(db, user_id)
        if volunteer is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Volunteer not found.")

        emergency = await EmergencyRequestRepository.get_active_for_volunteer(db, volunteer.id)
        if emergency is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No active emergency found.")

        return await EmergencyRequestService.get_emergency_status(db, emergency.id)