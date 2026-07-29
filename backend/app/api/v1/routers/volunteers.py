from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.core.dependencies import require_volunteer
from app.models.user import User
from app.schemas.location import LocationUpdateRequest
from app.services.volunteer_service import VolunteerService

router = APIRouter(
    prefix="/volunteers",
    tags=["Volunteers"],
)


@router.get("/profile")
async def get_profile(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):
    return await VolunteerService.get_profile(
        db,
        current_user.id,
    )
    
@router.put("/home-location")
async def update_home_location(
    data: LocationUpdateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):
    return await VolunteerService.update_home_location(
        db,
        current_user.id,
        data,
    )