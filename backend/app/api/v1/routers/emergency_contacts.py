from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.emergency_contact_service import (
    EmergencyContactService,
)
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