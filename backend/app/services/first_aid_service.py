from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.first_aid_repository import FirstAidRepository


class FirstAidService:

    @staticmethod
    async def get_all_categories(
        db: AsyncSession,
    ):
        categories = await FirstAidRepository.get_all_categories(db)

        return [
            {
                "id": category.id,
                "name_en": category.name_en,
                "name_mm": category.name_mm,
                "priority": category.priority,
                "steps": [
                    {
                        "id": step.id,
                        "category_id": step.category_id,
                        "step_number": step.step_number,
                        "instruction_en": step.instruction_en,
                        "instruction_mm": step.instruction_mm,
                    }
                    for step in category.first_aid_steps
                ],
            }
            for category in categories
        ]

    @staticmethod
    async def get_category(
        db: AsyncSession,
        category_id: int,
    ):
        category = await FirstAidRepository.get_category_by_id(
            db,
            category_id,
        )

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Emergency category not found",
            )

        return {
            "id": category.id,
            "name_en": category.name_en,
            "name_mm": category.name_mm,
            "priority": category.priority,
            "steps": [
                {
                    "id": step.id,
                    "category_id": step.category_id,
                    "step_number": step.step_number,
                    "instruction_en": step.instruction_en,
                    "instruction_mm": step.instruction_mm,
                }
                for step in category.first_aid_steps
            ],
        }