from uuid import UUID
from datetime import datetime, timezone

from sqlalchemy import func, select, update, cast
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from geoalchemy2 import Geometry

from app.models.emergency_request import EmergencyRequest
from app.models.enums import EmergencyStatus
from app.models.volunteer import Volunteer
from app.models.current_volunteer_location import CurrentVolunteerLocation

class EmergencyRequestRepository:
    @staticmethod
    async def create(
        db: AsyncSession, 
        emergency: EmergencyRequest
    ) -> EmergencyRequest:
        db.add(emergency)
        await db.flush()
        return emergency

    @staticmethod
    async def get_by_id(
        db: AsyncSession, 
        emergency_id: UUID
    ) -> EmergencyRequest | None:
        result = await db.execute(
            select(EmergencyRequest)
            .where(EmergencyRequest.id == emergency_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def update_status(
        db: AsyncSession, 
        emergency_id: UUID, 
        status: EmergencyStatus
    ) -> EmergencyRequest | None:
        result = await db.execute(
            update(EmergencyRequest)
            .where(EmergencyRequest.id == emergency_id)
            .values(status=status)
            .returning(EmergencyRequest)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def assign_volunteer(
        db: AsyncSession, 
        emergency: EmergencyRequest, 
        volunteer_id: UUID
    ) -> EmergencyRequest:
        emergency.assigned_volunteer_id = volunteer_id
        emergency.status = EmergencyStatus.ASSIGNED
        emergency.accepted_at = datetime.now(timezone.utc)
        
        await db.flush()
        await db.refresh(emergency)
        return emergency

    @staticmethod
    async def get_status_with_volunteer(
        db: AsyncSession, 
        emergency_id: UUID
    ):
        vol_geom = cast(CurrentVolunteerLocation.location, Geometry)
        
        query = (
            select(
                EmergencyRequest,
                func.ST_Y(vol_geom).label("volunteer_latitude"),
                func.ST_X(vol_geom).label("volunteer_longitude"),
                CurrentVolunteerLocation.speed.label("volunteer_speed"),
                CurrentVolunteerLocation.heading.label("volunteer_heading"),
                func.ST_Distance(
                    EmergencyRequest.location, 
                    CurrentVolunteerLocation.location
                ).label("distance_meters"),
            )
            .outerjoin(
                Volunteer, 
                EmergencyRequest.assigned_volunteer_id == Volunteer.id
            )
            .outerjoin(
                CurrentVolunteerLocation, 
                Volunteer.id == CurrentVolunteerLocation.volunteer_id
            )
            .options(
                selectinload(EmergencyRequest.category),
                selectinload(EmergencyRequest.assigned_volunteer).selectinload(Volunteer.user)
            )
            .where(EmergencyRequest.id == emergency_id)
        )
        
        result = await db.execute(query)
        return result.one_or_none()