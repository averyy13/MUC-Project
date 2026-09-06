from fastapi import HTTPException
from uuid import UUID
from datetime import datetime, timezone
from sqlalchemy import func, select, update, cast, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from geoalchemy2 import Geometry

from app.models.enums import AssignmentStatus, EmergencyStatus
from app.models.emergency_request import EmergencyRequest
from app.models.volunteer import Volunteer
from app.models.current_volunteer_location import CurrentVolunteerLocation
from app.repositories.volunteer_assignment_repository import VolunteerAssignmentRepository

class EmergencyRequestRepository:
    
    @staticmethod
    async def create(db: AsyncSession, emergency: EmergencyRequest) -> EmergencyRequest:
        db.add(emergency)
        await db.flush()
        return emergency

    @staticmethod
    async def get_by_id(db: AsyncSession, emergency_id: UUID) -> EmergencyRequest | None:
        result = await db.execute(select(EmergencyRequest).where(EmergencyRequest.id == emergency_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def update_status(db: AsyncSession, emergency_id: UUID, status: EmergencyStatus) -> EmergencyRequest | None:
        result = await db.execute(update(EmergencyRequest).where(EmergencyRequest.id == emergency_id).values(status=status).returning(EmergencyRequest))
        return result.scalar_one_or_none()

    @staticmethod
    async def assign_volunteer(db: AsyncSession, emergency: EmergencyRequest, volunteer_id):
        emergency.assigned_volunteer_id = volunteer_id
        emergency.status = EmergencyStatus.ASSIGNED
        emergency.accepted_at = datetime.now(timezone.utc)
        
        await db.flush()
        await db.refresh(emergency)
        
        return emergency

    @staticmethod
    async def get_status_with_volunteer(db: AsyncSession, emergency_id: UUID):
        vol_geom = cast(CurrentVolunteerLocation.location, Geometry)
        query = (
            select(
                EmergencyRequest,
                func.ST_Y(vol_geom).label("volunteer_latitude"),
                func.ST_X(vol_geom).label("volunteer_longitude"),
                CurrentVolunteerLocation.speed.label("volunteer_speed"),
                CurrentVolunteerLocation.heading.label("volunteer_heading"),
                func.ST_Distance(EmergencyRequest.location, CurrentVolunteerLocation.location).label("distance_meters"),
                CurrentVolunteerLocation.updated_at.label("location_updated_at"),
            )
            .outerjoin(Volunteer, EmergencyRequest.assigned_volunteer_id == Volunteer.id)
            .outerjoin(CurrentVolunteerLocation, Volunteer.id == CurrentVolunteerLocation.volunteer_id)
            .options(selectinload(EmergencyRequest.category), selectinload(EmergencyRequest.assigned_volunteer).selectinload(Volunteer.user))
            .where(EmergencyRequest.id == emergency_id)
        )
        result = await db.execute(query)
        return result.one_or_none()
    
    @staticmethod
    async def start_rescue(db: AsyncSession, emergency: EmergencyRequest, volunteer_id):
        if emergency.assigned_volunteer_id != volunteer_id:
            raise HTTPException(status_code=403, detail="You are not assigned to this emergency")
        if emergency.status != EmergencyStatus.ASSIGNED:
            raise HTTPException(status_code=409, detail=f"Emergency cannot start rescue from status {emergency.status.value}")
        
        assignment = await VolunteerAssignmentRepository.get_for_request_and_volunteer(db, emergency.id, volunteer_id)
        if assignment is None:
            raise HTTPException(status_code=404, detail="Volunteer assignment not found")
        if assignment.status != AssignmentStatus.ACCEPTED:
            raise HTTPException(status_code=409, detail="Volunteer assignment is not accepted")

        emergency.status = EmergencyStatus.VOLUNTEER_EN_ROUTE
        await db.flush()
        await db.refresh(emergency)
        return emergency
    
    @staticmethod
    async def get_location(db: AsyncSession, emergency_id):
        result = await db.execute(
            text("SELECT ST_Y(location::geometry) AS latitude, ST_X(location::geometry) AS longitude FROM emergency_requests WHERE id = :emergency_id"),
            {"emergency_id": emergency_id}
        )
        row = result.mappings().first()
        return dict(row) if row else None
    
    @staticmethod
    async def get_assigned_volunteer_id(db: AsyncSession, emergency_id):
        result = await db.execute(
            text("SELECT assigned_volunteer_id FROM emergency_requests WHERE id = :emergency_id"),
            {"emergency_id": emergency_id}
        )
        row = result.mappings().first()
        return row["assigned_volunteer_id"] if row else None
    
    @staticmethod
    async def mark_arrived(db: AsyncSession, emergency: EmergencyRequest, volunteer_id):
        if emergency.assigned_volunteer_id != volunteer_id:
            raise HTTPException(status_code=403, detail="You are not assigned to this emergency")
        if emergency.status != EmergencyStatus.VOLUNTEER_EN_ROUTE:
            raise HTTPException(status_code=409, detail=f"Emergency cannot be marked arrived from status {emergency.status.value}")
        
        assignment = await VolunteerAssignmentRepository.get_for_request_and_volunteer(db, emergency.id, volunteer_id)
        if assignment is None:
            raise HTTPException(status_code=404, detail="Volunteer assignment not found")
        if assignment.status != AssignmentStatus.ACCEPTED:
            raise HTTPException(status_code=409, detail="Volunteer assignment is not active")

        assignment.status = AssignmentStatus.ARRIVED
        assignment.arrived_at = datetime.now(timezone.utc)
        await db.flush()
        await db.refresh(emergency)
        return emergency   

    @staticmethod
    async def complete_rescue(db: AsyncSession, emergency: EmergencyRequest, volunteer_id):
        if emergency.assigned_volunteer_id != volunteer_id:
            raise HTTPException(status_code=403, detail="You are not assigned to this emergency")  
        if emergency.status != EmergencyStatus.VOLUNTEER_EN_ROUTE:
            raise HTTPException(status_code=409, detail=f"Emergency cannot be completed from status {emergency.status.value}")    
        
        assignment = await VolunteerAssignmentRepository.get_for_request_and_volunteer(db, emergency.id, volunteer_id)
        if assignment is None:
            raise HTTPException(status_code=404, detail="Volunteer assignment not found")
        if assignment.status != AssignmentStatus.ARRIVED:
            raise HTTPException(status_code=409, detail="Volunteer must arrive before completing rescue")  

        assignment.status = AssignmentStatus.COMPLETED
        assignment.completed_at = datetime.now(timezone.utc)
        emergency.status = EmergencyStatus.COMPLETED
        
        await db.flush()
        await db.refresh(emergency)
        return emergency
    
    @staticmethod
    async def cancel_emergency(
        db: AsyncSession,
        emergency: EmergencyRequest,
    ):
        if emergency.status in (
            EmergencyStatus.COMPLETED,
            EmergencyStatus.CANCELLED,
        ):
            raise HTTPException(
                status_code=409,
                detail=(
                    f"Emergency cannot be cancelled "
                    f"from status {emergency.status.value}"
                ),
            )

        emergency.status = EmergencyStatus.CANCELLED

        await db.flush()
        await db.refresh(emergency)

        return emergency
    
    @staticmethod
    async def get_active_for_device(
        db: AsyncSession,
        device_id: UUID,
    ) -> EmergencyRequest | None:
    
        result = await db.execute(
            select(EmergencyRequest)
            .where(
                EmergencyRequest.device_id == device_id,
                EmergencyRequest.status.in_(
                    [
                        EmergencyStatus.SEARCHING,
                        EmergencyStatus.ASSIGNED,
                        EmergencyStatus.VOLUNTEER_EN_ROUTE,
                    ]
                ),
            )
            .order_by(
                EmergencyRequest.created_at.desc()
            )
            .limit(1)
        )
    
        return result.scalar_one_or_none()