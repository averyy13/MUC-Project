from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.models.volunteer import Volunteer
from app.models.enums import ApprovalStatus
from app.models import volunteer

class AdminRepository:

    @staticmethod
    async def get_volunteers_by_status(
        db: AsyncSession,
        status: ApprovalStatus
    ):
        from app.models.volunteer_assignment import VolunteerAssignment
        from sqlalchemy import func

        rescue_counts = (
            select(
                VolunteerAssignment.volunteer_id,
                func.count(func.distinct(VolunteerAssignment.request_id)).label("completed_rescues")
            )
            .where(VolunteerAssignment.completed_at.is_not(None))
            .group_by(VolunteerAssignment.volunteer_id)
            .subquery()
        )

        query = (
            select(
                Volunteer,
                func.coalesce(rescue_counts.c.completed_rescues, 0).label("completed_rescues")
            )
            .options(selectinload(Volunteer.user))
            .outerjoin(rescue_counts, Volunteer.id == rescue_counts.c.volunteer_id)
            .where(Volunteer.approval_status == status)
        )

        result = await db.execute(query)
        return result.all()


    @staticmethod
    async def get_volunteer(
        db: AsyncSession,
        volunteer_id
    ):

        result = await db.execute(
            select(Volunteer)
            .options(selectinload(Volunteer.user))
            .where(Volunteer.id == volunteer_id)
        )

        return result.scalar_one_or_none()
    
    @staticmethod
    async def update_status(
        db: AsyncSession,
        volunteer: Volunteer,
        status: ApprovalStatus,
    ):
        volunteer.approval_status = status
        await db.flush()
        return volunteer