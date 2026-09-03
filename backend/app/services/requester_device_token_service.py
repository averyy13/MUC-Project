from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.requester_device_token_repository import (
    RequesterDeviceTokenRepository,
)

class RequesterDeviceTokenService:

    @staticmethod
    async def register_token(
        db: AsyncSession,
        device_id: UUID,
        fcm_token: str,
        platform: str,
    ):
        try:
            token_platform = platform.upper()

            token = await RequesterDeviceTokenRepository.upsert(
                db=db,
                device_id=device_id,
                fcm_token=fcm_token,
                platform=token_platform,
            )

            await db.commit()

            return {
                "device_id": token.device_id,
                "message": "Requester FCM token registered successfully.",
            }

        except Exception as exc:
            await db.rollback()

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to register requester FCM token.",
            ) from exc