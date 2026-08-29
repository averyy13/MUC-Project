from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.emergency_contact_service import (
    EmergencyContactService,
)
from uuid import UUID
from app.schemas.emergency_contact import RescueRouteResponse

router = APIRouter(
    prefix="/emergency-contacts",
    tags=["Emergency Contacts"],
)

@router.get("/nearby")
async def get_nearby_rescue_teams(
    latitude: float = Query(
        ...,
        ge=-90,
        le=90,
    ),
    longitude: float = Query(
        ...,
        ge=-180,
        le=180,
    ),
    limit: int = Query(
        5,
        ge=1,
        le=20,
    ),
    db: AsyncSession = Depends(get_db),
):
    return await EmergencyContactService.get_nearby_rescue_teams(
        db=db,
        latitude=latitude,
        longitude=longitude,
        limit=limit,
    )
    
@router.get(
    "/{contact_id}/route",
    response_model=RescueRouteResponse,
)
async def get_rescue_route(
    contact_id: UUID,
    latitude: float = Query(..., ge=-90, le=90),
    longitude: float = Query(..., ge=-180, le=180),
    db: AsyncSession = Depends(get_db),
):
    return await EmergencyContactService.get_route_to_contact(
        db=db,
        contact_id=contact_id,
        user_latitude=latitude,
        user_longitude=longitude,
    )