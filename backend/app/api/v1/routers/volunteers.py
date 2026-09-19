from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.core.dependencies import require_volunteer
from app.models.user import User
from app.schemas.location import LocationUpdateRequest
from app.services.volunteer_service import VolunteerService
from app import db
from app.schemas.location import (LocationUpdateRequest, AvailabilityUpdateRequest, )
from app.schemas.device_token import DeviceTokenRegisterRequest, DeviceTokenResponse
from app.services.device_token_service import DeviceTokenService
from app.schemas.emergency_request import EmergencyStatusResponse
from app.schemas.rescue_history import RescueHistoryResponse

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
    
@router.post("/me/device-token", response_model=DeviceTokenResponse,)
async def register_device_token(
    request: DeviceTokenRegisterRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):
    return await DeviceTokenService.register_token(
        db=db,
        user_id=current_user.id,
        fcm_token=request.fcm_token,
        platform=request.platform,
    )

@router.get( "/me/active-emergency",response_model=EmergencyStatusResponse | None,)
async def get_active_emergency(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):
    return await VolunteerService.get_active_emergency_for_volunteer(
        db=db,
        user_id=current_user.id,
    )
@router.get(
    "/me/rescue-history",response_model=list[RescueHistoryResponse],
)
async def get_rescue_history(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):
    return await VolunteerService.get_rescue_history(
        db=db,
        user_id=current_user.id,
    )   
