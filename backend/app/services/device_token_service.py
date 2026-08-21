from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.device_token_repository import (
    DeviceTokenRepository,
)
from app.repositories.volunteer_repository import (
    VolunteerRepository,
)


class DeviceTokenService:

    @staticmethod
    async def register_token(
        db: AsyncSession,
        user_id,
        fcm_token: str,
        platform: str = "ANDROID",
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

        if volunteer.approval_status.value != "APPROVED":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only approved volunteers can register a device",
            )

        await DeviceTokenRepository.upsert(
            db=db,
            volunteer_id=volunteer.id,
            fcm_token=fcm_token,
            platform=platform,
        )

        await db.commit()

        return {
            "message": "Device token registered successfully.",
        }