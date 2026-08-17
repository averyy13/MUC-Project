from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.medical_facility_service import (
    MedicalFacilityService,
)

router = APIRouter(
    prefix="/facilities",
    tags=["Medical Facilities"],
)

@router.get("/nearby")
async def get_nearby_facilities(
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
    return await MedicalFacilityService.get_nearby_facilities(
        db,
        latitude,
        longitude,
        limit,
    )