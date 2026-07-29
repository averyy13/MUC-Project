from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.emergency_category import EmergencyCategoryResponse
from app.services.emergency_category_service import (
    EmergencyCategoryService,
)

router = APIRouter(
    prefix="/emergency-categories",
    tags=["Emergency Categories"],
)


@router.get(
    "",
    response_model=List[EmergencyCategoryResponse],
)
async def get_categories(
    db: AsyncSession = Depends(get_db),
):

    return await EmergencyCategoryService.get_all_categories(db)