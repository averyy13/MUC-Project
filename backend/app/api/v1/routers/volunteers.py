from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.core.dependencies import require_volunteer
from app.models.user import User
from app.schemas.location import LocationUpdateRequest
from app.services.volunteer_service import VolunteerService
from app import db
from app.schemas.location import (LocationUpdateRequest, AvailabilityUpdateRequest, )


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
    
@router.patch("/me/location")
async def update_current_location(
    data: LocationUpdateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):
    return await VolunteerService.update_current_location(
        db,
        current_user.id,
        data,
    )
    
@router.patch("/me/availability")
async def update_availability(
    data: AvailabilityUpdateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):
    return await VolunteerService.update_availability(
        db,
        current_user.id,
        data.availability,
    )