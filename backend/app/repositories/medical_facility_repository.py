from sqlalchemy import select, func, cast
from sqlalchemy.ext.asyncio import AsyncSession
from geoalchemy2 import Geography, Geometry

from app.models.medical_facility import MedicalFacility


class MedicalFacilityRepository:

    @staticmethod
    async def get_nearby_facilities(
        db: AsyncSession,
        latitude: float,
        longitude: float,
        limit: int = 5,
    ):
        # ---------------------------------------------------------
        # User's current GPS location
        # ---------------------------------------------------------
        user_location = func.ST_SetSRID(
            func.ST_MakePoint(
                longitude,
                latitude,
            ),
            4326,
        )

        # Convert user's geometry point to geography
        user_location = cast(
            user_location,
            Geography("POINT", srid=4326),
        )

        # ---------------------------------------------------------
        # Distance between user and facility
        # ST_Distance(geography, geography) returns meters
        # ---------------------------------------------------------
        distance_meters = func.ST_Distance(
            MedicalFacility.location,
            user_location,
        )

        # ---------------------------------------------------------
        # Extract facility latitude/longitude
        # Geography -> Geometry
        # ---------------------------------------------------------
        location_geometry = cast(
            MedicalFacility.location,
            Geometry("POINT", srid=4326),
        )

        latitude_result = func.ST_Y(location_geometry)
        longitude_result = func.ST_X(location_geometry)

        # ---------------------------------------------------------
        # Query
        # ---------------------------------------------------------
        query = (
            select(
                MedicalFacility,
                distance_meters.label("distance_meters"),
                latitude_result.label("latitude"),
                longitude_result.label("longitude"),
            )
            .where(
                MedicalFacility.is_active.is_(True)
            )
            .order_by(distance_meters)
            .limit(limit)
        )

        result = await db.execute(query)

        return result.all()