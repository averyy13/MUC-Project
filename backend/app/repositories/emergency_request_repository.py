from uuid import UUID
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.emergency_request import EmergencyRequest
from app.models.enums import EmergencyStatus


class EmergencyRequestRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        emergency: EmergencyRequest,
    ) -> EmergencyRequest:
        db.add(emergency)
        await db.flush()
        return emergency

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        emergency_id: UUID,
    ) -> EmergencyRequest | None:
        result = await db.execute(
            select(EmergencyRequest).where(EmergencyRequest.id == emergency_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def update_status(
        db: AsyncSession,
        emergency_id: UUID,
        status: EmergencyStatus,
    ) -> EmergencyRequest | None:
        result = await db.execute(
            update(EmergencyRequest)
            .where(EmergencyRequest.id == emergency_id)
            .values(status=status)
            .returning(EmergencyRequest)
        )
        return result.scalar_one_or_none()