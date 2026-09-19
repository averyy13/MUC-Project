from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.volunteer_repository import VolunteerRepository
from app.schemas.location import LocationUpdateRequest
from app.repositories.emergency_request_repository import EmergencyRequestRepository
from app.repositories.volunteer_assignment_repository import VolunteerAssignmentRepository
from app.services.emergency_request_service import EmergencyRequestService

class VolunteerService:
    @staticmethod
    async def get_profile(
        db: AsyncSession,
        user_id,
    ):
        volunteer = await VolunteerRepository.get_by_user_id(
            db,
            user_id,
        )

        if volunteer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Volunteer not found",
            )
        home_location = await VolunteerRepository.get_home_location(db, volunteer.id)
        current_location = await VolunteerRepository.get_current_location(db, volunteer.id)
        completed_rescues = await VolunteerAssignmentRepository.count_completed_for_volunteer(db, volunteer.id)
        
        return {
            "volunteer_id": volunteer.id,
            "user_id": volunteer.user.id,
            "full_name": volunteer.user.full_name,
            "phone": volunteer.user.phone,
            "email": volunteer.user.email,
            "nrc_number": volunteer.nrc_number,
            "address": volunteer.address,
            "approval_status": volunteer.approval_status.value,
            "availability": volunteer.availability,
            "certificate_url": volunteer.certificate_url,
            "home_location": home_location,
            "current_location": current_location,
            "completed_rescues": completed_rescues,
        }

    @staticmethod
    async def update_home_location(
        db: AsyncSession,
        user_id,
        location: LocationUpdateRequest,
    ):
        volunteer = await VolunteerRepository.get_by_user_id(
            db,
            user_id,
        )

        if volunteer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Volunteer not found",
            )

        await VolunteerRepository.update_home_location(
            db=db,
            volunteer_id=volunteer.id,
            latitude=location.latitude,
            longitude=location.longitude,
        )

        return {
            "message": "Home location updated successfully."
        }

    @staticmethod
    async def update_current_location(
        db: AsyncSession,
        user_id,
        location: LocationUpdateRequest,
    ):
        volunteer = await VolunteerRepository.get_by_user_id(
            db,
            user_id,
        )

        if volunteer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Volunteer not found",
            )

        await VolunteerRepository.update_current_location(
            db=db,
            volunteer_id=volunteer.id,
            latitude=location.latitude,
            longitude=location.longitude,
        )

        await db.commit()
        return {
            "message": "Current location updated successfully."
        }

    @staticmethod
    async def get_current_location(
        db: AsyncSession,
        user_id,
    ):
        volunteer = await VolunteerRepository.get_by_user_id(
            db,
            user_id,
        )

        if volunteer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Volunteer not found",
            )

        location = await VolunteerRepository.get_current_location(
            db,
            volunteer.id,
        )

        if location is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Current location not found.",
            )

        return location

    @staticmethod
    async def update_availability(
        db: AsyncSession,
        user_id,
        availability: bool,
    ):
        volunteer = await VolunteerRepository.get_by_user_id(db, user_id)  

        if volunteer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Volunteer not found",
            )

        await VolunteerRepository.update_availability(
            db,
            volunteer.id,
            availability,
        )

        return {
            "message": "Availability updated successfully.",
            "availability": availability,
        }
        
    @staticmethod
    async def get_active_emergency_for_volunteer(
        db: AsyncSession,
        user_id,
    ):
        volunteer = await VolunteerRepository.get_by_user_id(db,
            user_id,
        )
    
        if volunteer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Volunteer not found",
            )
    
        assignment = await VolunteerAssignmentRepository.get_active_for_volunteer(
            db,
            volunteer.id,
        )
    
        if assignment is None:
            return None
    
        return await EmergencyRequestService.get_emergency_status(
            db,
            assignment.request_id,
        )
        
    @staticmethod
    async def get_rescue_history(db: AsyncSession, user_id):
        volunteer = await VolunteerRepository.get_by_user_id(db, user_id)
        if not volunteer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Volunteer not found")
    
        records = await VolunteerAssignmentRepository.get_completed_for_volunteer(db=db, volunteer_id=volunteer.id)
    
        return [{
            "emergency_id": emergency.id,
            "category_id": category.id,
            "category_name_en": category.name_en,
            "category_name_mm": category.name_mm,
            "description": emergency.description,
            "latitude": float(latitude),
            "longitude": float(longitude),
            "completed_at": assignment.completed_at,
        } for assignment, emergency, category, latitude, longitude in records]