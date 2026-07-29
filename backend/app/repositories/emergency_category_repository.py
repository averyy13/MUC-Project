
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.emergency_category import EmergencyCategory


class EmergencyCategoryRepository:

    @staticmethod
    async def get_all(db: AsyncSession):

        result = await db.execute(
            select(EmergencyCategory).order_by(EmergencyCategory.priority)
        )

        return result.scalars().all()