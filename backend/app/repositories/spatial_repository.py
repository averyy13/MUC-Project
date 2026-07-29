from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.spatial_queries import (
    FIND_NEAREST_MEDICAL_FACILITIES,
    FIND_NEAREST_RESCUE_CONTACTS,
    FIND_NEAREST_VOLUNTEERS,
)


class SpatialRepository:

    @staticmethod
    async def nearest_volunteers(
        db: AsyncSession,
        latitude: float,
        longitude: float,
        limit: int = 20,
    ):

        result = await db.execute(
            text(FIND_NEAREST_VOLUNTEERS),
            {
                "latitude": latitude,
                "longitude": longitude,
                "limit": limit,
            },
        )

        return result.mappings().all()


    @staticmethod
    async def nearest_rescue_contacts(
        db: AsyncSession,
        latitude: float,
        longitude: float,
        limit: int = 3,
    ):

        result = await db.execute(
            text(FIND_NEAREST_RESCUE_CONTACTS),
            {
                "latitude": latitude,
                "longitude": longitude,
                "limit": limit,
            },
        )

        return result.mappings().all()


    @staticmethod
    async def nearest_facilities(
        db: AsyncSession,
        latitude: float,
        longitude: float,
        limit: int = 5,
    ):

        result = await db.execute(
            text(FIND_NEAREST_MEDICAL_FACILITIES),
            {
                "latitude": latitude,
                "longitude": longitude,
                "limit": limit,
            },
        )

        return result.mappings().all()