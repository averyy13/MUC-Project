from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.repositories.spatial_repository import SpatialRepository

router = APIRouter(
    prefix="/spatial",
    tags=["Spatial Test"],
)


@router.get("/nearby")
async def nearby(
    latitude: float,
    longitude: float,
    db: AsyncSession = Depends(get_db),
):

    volunteers = await SpatialRepository.nearest_volunteers(
        db, latitude, longitude, 5
    )

    rescue = await SpatialRepository.nearest_rescue_contacts(
        db, latitude, longitude, 3
    )

    facilities = await SpatialRepository.nearest_facilities(
        db, latitude, longitude, 5
    )

    return {
        "volunteers": volunteers,
        "rescue_contacts": rescue,
        "medical_facilities": facilities,
    }