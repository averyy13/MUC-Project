from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.models.volunteer import Volunteer
from app.models.enums import ApprovalStatus


class AdminRepository:

    @staticmethod
    async def get_volunteers_by_status(
        db: AsyncSession,
        status: ApprovalStatus
    ):

        result = await db.execute(
            select(Volunteer)
            .options(selectinload(Volunteer.user))
            .where(Volunteer.approval_status == status)
        )

        return result.scalars().all()


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