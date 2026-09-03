from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.requester_device_token import RequesterDeviceToken


class RequesterDeviceTokenRepository:

    @staticmethod
    async def get_by_device_id(
        db: AsyncSession,
        device_id: UUID,
    ) -> RequesterDeviceToken | None:

        result = await db.execute(
            select(RequesterDeviceToken).where(
                RequesterDeviceToken.device_id == device_id
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def upsert(
        db: AsyncSession,
        device_id: UUID,
        fcm_token: str,
        platform,
    ) -> RequesterDeviceToken:

        existing = await RequesterDeviceTokenRepository.get_by_device_id(
            db,
            device_id,
        )

        if existing is not None:
            existing.fcm_token = fcm_token
            existing.platform = platform

            await db.flush()
            return existing

        token = RequesterDeviceToken(
            device_id=device_id,
            fcm_token=fcm_token,
            platform=platform,
        )

        db.add(token)
        await db.flush()

        return token