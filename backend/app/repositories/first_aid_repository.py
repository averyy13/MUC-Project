from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.emergency_category import EmergencyCategory


class FirstAidRepository:

    @staticmethod
    async def get_all_categories(
        db: AsyncSession,
    ):
        result = await db.execute(
            select(EmergencyCategory)
            .options(
                selectinload(
                    EmergencyCategory.first_aid_steps
                )
            )
            .order_by(EmergencyCategory.priority)
        )

        return result.scalars().all()

    @staticmethod
    async def get_category_by_id(
        db: AsyncSession,
        category_id: int,
    ):
        result = await db.execute(
            select(EmergencyCategory)
            .options(
                selectinload(
                    EmergencyCategory.first_aid_steps
                )
            )
            .where(
                EmergencyCategory.id == category_id
            )
        )

        return result.scalar_one_or_none()