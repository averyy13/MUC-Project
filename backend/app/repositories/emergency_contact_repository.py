from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.emergency_contact import EmergencyContact


class EmergencyContactRepository:

    @staticmethod
    async def get_nearby_rescue_teams(
        db: AsyncSession,
        latitude: float,
        longitude: float,
        limit: int = 5,
    ):
        user_location = func.ST_SetSRID(
            func.ST_MakePoint(
                longitude,
                latitude,
            ),
            4326,
        )

        distance_meters = func.ST_Distance(
            EmergencyContact.location,
            user_location,
        )

        longitude_result = func.ST_X(
            func.ST_GeomFromEWKB(
                func.ST_AsEWKB(
                    EmergencyContact.location
                )
            )
        )

        latitude_result = func.ST_Y(
            func.ST_GeomFromEWKB(
                func.ST_AsEWKB(
                    EmergencyContact.location
                )
            )
        )

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