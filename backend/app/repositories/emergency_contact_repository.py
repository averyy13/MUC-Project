from sqlalchemy import select, func, cast
from sqlalchemy.ext.asyncio import AsyncSession
from geoalchemy2 import Geography, Geometry  # <-- Added Geometry here

from app.models.emergency_contact import EmergencyContact

class EmergencyContactRepository:

    @staticmethod
    async def get_nearby_rescue_teams(
        db: AsyncSession,
        latitude: float,
        longitude: float,
        limit: int = 5,
    ):
        # Create user's location as GEOMETRY first
        user_location_geometry = func.ST_SetSRID(
            func.ST_MakePoint(
                longitude,
                latitude,
            ),
            4326,
        )

        # Explicitly convert it to GEOGRAPHY
        # because EmergencyContact.location is GEOGRAPHY.
        user_location = cast(
            user_location_geometry,
            Geography(
                geometry_type="POINT",
                srid=4326,
            ),
        )

        # Distance in meters because both values are GEOGRAPHY.
        distance_meters = func.ST_Distance(
            EmergencyContact.location,
            user_location,
        )

        # ---------------------------------------------------------
        # FIX: Cast Geography to Geometry to safely extract X and Y
        # ---------------------------------------------------------
        location_as_geometry = cast(EmergencyContact.location, Geometry)

        # Extract longitude from the geometry point.
        longitude_result = func.ST_X(location_as_geometry)

        # Extract latitude from the geometry point.
        latitude_result = func.ST_Y(location_as_geometry)

        query = (
            select(
                EmergencyContact,
                distance_meters.label("distance_meters"),
                latitude_result.label("latitude"),
                longitude_result.label("longitude"),
            )
            .where(
                EmergencyContact.is_active.is_(True)
            )
            .order_by(distance_meters)
            .limit(limit)
        )

        result = await db.execute(query)

        return result.all()