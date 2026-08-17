from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.first_aid import (
    FirstAidCategoryResponse,
)
from app.services.first_aid_service import FirstAidService


router = APIRouter(
    prefix="/first-aid",
    tags=["First Aid"],
)


@router.get(
    "/categories",
    response_model=list[FirstAidCategoryResponse],
)
async def get_first_aid_categories(
    db: AsyncSession = Depends(get_db),
):
    return await FirstAidService.get_all_categories(db)


@router.get(
    "/categories/{category_id}",
    response_model=FirstAidCategoryResponse,
)
async def get_first_aid_category(
    category_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await FirstAidService.get_category(
        db,
        category_id,
    )