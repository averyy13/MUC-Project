
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.emergency_category_repository import (
    EmergencyCategoryRepository,
)


class EmergencyCategoryService:

    @staticmethod
    async def get_all_categories(db: AsyncSession):

        return await EmergencyCategoryRepository.get_all(db)