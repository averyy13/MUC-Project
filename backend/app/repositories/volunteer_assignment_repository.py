from __future__ import annotations
from datetime import datetime, timezone
from unittest import result
from uuid import UUID
from geoalchemy2 import Geometry
from sqlalchemy import cast, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.enums import AssignmentStatus
from app.models.volunteer_assignment import VolunteerAssignment
from app.models.emergency_category import EmergencyCategory
from app.models.emergency_request import EmergencyRequest

class VolunteerAssignmentRepository:
    @staticmethod
    async def create(
        db: AsyncSession,
        request_id: UUID,
        volunteer_id: UUID,
        notification_round: int = 1,
    ) -> VolunteerAssignment:
        assignment = VolunteerAssignment(
            request_id=request_id,
            volunteer_id=volunteer_id,
            notification_round=notification_round,
            status=AssignmentStatus.PENDING,
        )
        db.add(assignment)
        await db.flush()
        return assignment
    
    @staticmethod
    async def get_for_request_and_volunteer(
        db: AsyncSession,
        request_id: UUID,
        volunteer_id: UUID,
    ) -> VolunteerAssignment | None:

        result = await db.execute(
            select(VolunteerAssignment).where(
                VolunteerAssignment.request_id == request_id,
                VolunteerAssignment.volunteer_id == volunteer_id,
            )
        )
        return result.scalar_one_or_none()
    
    @staticmethod
    async def accept(
        db: AsyncSession,
        assignment: VolunteerAssignment,
    ) -> VolunteerAssignment:
        assignment.status = AssignmentStatus.ACCEPTED
        assignment.accepted_at = datetime.now(timezone.utc)
        await db.flush()
        return assignment
    
    @staticmethod
    async def mark_arrived(
        db: AsyncSession,
        assignment: VolunteerAssignment,
    ) -> VolunteerAssignment:
        assignment.status = AssignmentStatus.ARRIVED
        assignment.arrived_at = datetime.now(timezone.utc)
        await db.flush()
        return assignment
    
    @staticmethod
    async def complete(
        db: AsyncSession,
        assignment: VolunteerAssignment,
    ) -> VolunteerAssignment:
        assignment.status = AssignmentStatus.COMPLETED
        assignment.completed_at = datetime.now(timezone.utc)
        await db.flush()
        return assignment
    
    @staticmethod
    async def get_active_for_volunteer(
        db: AsyncSession,
        volunteer_id: UUID,
    ):
        result = await db.execute(
            select(VolunteerAssignment)
            .where(
                VolunteerAssignment.volunteer_id == volunteer_id,
                VolunteerAssignment.status.in_(
                    [
                        AssignmentStatus.ACCEPTED,
                        AssignmentStatus.ARRIVED,
                    ]
                ),
            )
            .order_by(
                VolunteerAssignment.accepted_at.desc()
            )
            .limit(1)
        )
        return result.scalar_one_or_none()
    
    @staticmethod
    async def count_completed_for_volunteer(
        db: AsyncSession,
        volunteer_id,
    ) -> int:

        result = await db.execute(
            select(func.count(VolunteerAssignment.id))
            .where(
                VolunteerAssignment.volunteer_id == volunteer_id,
                VolunteerAssignment.status == AssignmentStatus.COMPLETED,
            )
        )
        return result.scalar_one()
    
    @staticmethod
    async def get_completed_for_volunteer(db: AsyncSession, volunteer_id: UUID):
        loc = cast(EmergencyRequest.location, Geometry("POINT", srid=4326))
        return (await db.execute(
            select(VolunteerAssignment, EmergencyRequest, EmergencyCategory, func.ST_Y(loc).label("latitude"), func.ST_X(loc).label("longitude"))
            .join(EmergencyRequest, VolunteerAssignment.request_id == EmergencyRequest.id)
            .join(EmergencyCategory, EmergencyRequest.category_id == EmergencyCategory.id)
            .where(VolunteerAssignment.volunteer_id == volunteer_id, VolunteerAssignment.status == AssignmentStatus.COMPLETED)
            .order_by(VolunteerAssignment.completed_at.desc())
        )).all()

    @staticmethod
    async def cancel(
        db: AsyncSession,
        assignment: VolunteerAssignment,
    ) -> VolunteerAssignment:
    
        if assignment.status in (
            AssignmentStatus.COMPLETED,
            AssignmentStatus.CANCELLED,
        ):
            return assignment
    
        assignment.status = AssignmentStatus.CANCELLED
    
        await db.flush()
    
        return assignment
    
    