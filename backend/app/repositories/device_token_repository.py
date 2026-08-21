from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.device_token import DeviceToken

class DeviceTokenRepository:
    @staticmethod
    async def upsert(
        db: AsyncSession,
        volunteer_id,
        fcm_token: str,
        platform,
    ) -> DeviceToken:
        
        # Check whether this FCM token already exists
        result = await db.execute(
            select(DeviceToken).where(
                DeviceToken.fcm_token == fcm_token
            )
        )
        device_token = result.scalar_one_or_none()

        if device_token:
            # Token exists. Update ownership in case they logged in with a different account.
            device_token.volunteer_id = volunteer_id
            device_token.platform = platform
        else:
            # Create a new token record
            device_token = DeviceToken(
                volunteer_id=volunteer_id,
                fcm_token=fcm_token,
                platform=platform,
            )
            db.add(device_token)

        await db.flush()
        return device_token

    @staticmethod
    async def delete_token(
        db: AsyncSession,
        fcm_token: str,
    ):
        result = await db.execute(
            select(DeviceToken).where(
                DeviceToken.fcm_token == fcm_token
            )
        )
        device_token = result.scalar_one_or_none()       
        if device_token:
            await db.delete(device_token)
            await db.flush()

    @staticmethod
    async def get_tokens_for_volunteer(
        db: AsyncSession,
        volunteer_id,
    ) -> list[str]:
        
        # Fetch all active tokens for this specific volunteer
        result = await db.execute(
            select(DeviceToken.fcm_token).where(
                DeviceToken.volunteer_id == volunteer_id
            )
        )
        return list(result.scalars().all())