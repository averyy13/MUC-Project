from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.volunteer_repository import VolunteerRepository
from app.schemas.location import LocationUpdateRequest


class VolunteerService:
    """
    Business logic for volunteer-related operations.
    """

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
        volunteer = await VolunteerRepository.get_by_user_id(
            db,
            user_id,
        )

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