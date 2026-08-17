from sqlalchemy import select, text,update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.volunteer import Volunteer


class VolunteerRepository:

    @staticmethod
    async def create_volunteer(db: AsyncSession, volunteer: Volunteer):
        db.add(volunteer)
        await db.flush()
        return volunteer

    @staticmethod
    async def get_by_user_id(db: AsyncSession, user_id):
        result = await db.execute(
            select(Volunteer)
            .options(selectinload(Volunteer.user))
            .where(Volunteer.user_id == user_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def update_home_location(
        db: AsyncSession,
        volunteer_id,
        latitude: float,
        longitude: float,
    ):
        await db.execute(
            text(
                "UPDATE volunteers "
                "SET home_location = ST_SetSRID(ST_MakePoint(:longitude, :latitude), 4326)::geography "
                "WHERE id = :volunteer_id"
            ),
            {
                "latitude": latitude,
                "longitude": longitude,
                "volunteer_id": volunteer_id,
            },
        )
        await db.commit()

    @staticmethod
    async def update_current_location(
        db: AsyncSession,
        volunteer_id,
        latitude: float,
        longitude: float,
    ):
        await db.execute(
            text(
                "INSERT INTO current_volunteer_locations (volunteer_id, location, updated_at) "
                "VALUES (:volunteer_id, ST_SetSRID(ST_MakePoint(:longitude, :latitude), 4326)::geography, NOW()) "
                "ON CONFLICT (volunteer_id) DO UPDATE SET location = EXCLUDED.location, updated_at = NOW()"
            ),
            {
                "volunteer_id": volunteer_id,
                "latitude": latitude,
                "longitude": longitude,
            },
        )


    @staticmethod
    async def get_home_location(db, volunteer_id):
        result = await db.execute(
            text(
                """
                SELECT
                    ST_Y(home_location::geometry) AS latitude,
                    ST_X(home_location::geometry) AS longitude
                FROM volunteers
                WHERE id = :volunteer_id
                """
            ),
            {"volunteer_id": volunteer_id},
        )

        row = result.mappings().first()
        return dict(row) if row else None

    @staticmethod
    async def get_current_location(db, volunteer_id):
        result = await db.execute(
            text(
                """
                SELECT
                    ST_Y(location::geometry) AS latitude,
                    ST_X(location::geometry) AS longitude,
                    updated_at
                FROM current_volunteer_locations
                WHERE volunteer_id = :volunteer_id
                """
            ),
            {"volunteer_id": volunteer_id},
        )

        row = result.mappings().first()
        return dict(row) if row else None

    @staticmethod
    async def update_availability(
        db: AsyncSession,
        volunteer_id,
        availability: bool,
    ):
        await db.execute(
            update(Volunteer)
            .where(Volunteer.id == volunteer_id)
            .values(availability=availability)
        )

        await db.commit()