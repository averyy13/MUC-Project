from uuid import UUID
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.medical_facility_service import (
    MedicalFacilityService,
)
from app.schemas.medical_facility import FacilityRouteResponse

router = APIRouter(
    prefix="/facilities",
    tags=["Medical Facilities"],
)

@router.get("/nearby")
async def get_nearby_facilities(
    latitude: float = Query(..., ge=-90, le=90),
    longitude: float = Query(..., ge=-180, le=180),
    limit: int = Query(5, ge=1, le=20),
    db: AsyncSession = Depends(get_db)
):
    return await MedicalFacilityService.get_nearby_facilities(db, latitude, longitude, limit)

@router.get("/{facility_id}/route",
    response_model=FacilityRouteResponse,
)
async def get_facility_route(
    facility_id: UUID,
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
    db: AsyncSession = Depends(get_db),
):
    return await MedicalFacilityService.get_route_to_facility(
        db=db,
        facility_id=facility_id,
        user_latitude=latitude,
        user_longitude=longitude,
    )