from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.volunteer import Volunteer
from app.models.user import User

class AuthRepository:

    @staticmethod
    async def get_user_by_phone(
        db: AsyncSession,
        phone: str
    ):
        result = await db.execute(
            select(User)
            .where(User.phone == phone)
        )

        return result.scalar_one_or_none()


    @staticmethod
    async def get_user_by_email(
        db: AsyncSession,
        email: str
    ):
        result = await db.execute(
            select(User)
            .where(User.email == email)
        )

        return result.scalar_one_or_none()


    @staticmethod
    async def create_user(
        db: AsyncSession,
        user: User
    ):

        db.add(user)
        await db.flush()
        return user

    @staticmethod
    async def get_user_with_volunteer(
    db: AsyncSession,
    phone: str
    ):
        result = await db.execute(
            select(User)
            .options(
                selectinload(User.volunteer)
             )
            .where(
                User.phone == phone
            )
        )
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_user_by_id(
        db: AsyncSession,
        user_id
    ):
        result = await db.execute(
            select(User)
            .where(User.id == user_id)
        )
        return result.scalar_one_or_none()