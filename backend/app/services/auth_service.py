from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token, hash_password, verify_password
from app.models.enums import ApprovalStatus, UserRole
from app.models.user import User
from app.models.volunteer import Volunteer
from app.repositories.auth_repository import AuthRepository
from app.repositories.volunteer_repository import VolunteerRepository
from app.schemas.auth import LoginRequest, VolunteerRegisterRequest


class AuthService:

    @staticmethod
    async def register_volunteer(
        db: AsyncSession,
        data: VolunteerRegisterRequest
    ):
        # Check duplicate phone
        existing_user = await AuthRepository.get_user_by_phone(
            db,
            data.phone
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Phone number already registered"
            )

        # Check duplicate email
        if data.email:
            existing_email = await AuthRepository.get_user_by_email(
                db,
                data.email
            )
            if existing_email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered"
                )

        user = User(
            full_name=data.full_name,
            phone=data.phone,
            email=data.email,
            password_hash=hash_password(data.password),
            role=UserRole.VOLUNTEER
        )

        await AuthRepository.create_user(
            db,
            user
        )

        volunteer = Volunteer(
            user_id=user.id,
            nrc_number=data.nrc_number,
            address=data.address,
            certificate_url=data.certificate_url,
            approval_status=ApprovalStatus.PENDING,
            availability=False
        )

        await VolunteerRepository.create_volunteer(
            db,
            volunteer
        )

        await db.commit()

        return {
            "message": "Volunteer registration submitted. Waiting for admin approval.",
            "user_id": str(user.id),
            "volunteer_id": str(volunteer.id)
        }

    @staticmethod
    async def login(
        db: AsyncSession,
        data: LoginRequest
    ):
        user = await AuthRepository.get_user_with_volunteer(
            db,
            data.phone
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid phone or password"
            )

        if not verify_password(
            data.password,
            user.password_hash
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid phone or password"
            )

        if user.role == UserRole.VOLUNTEER:
            if user.volunteer is None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Volunteer profile not found"
                )

            if user.volunteer.approval_status != ApprovalStatus.APPROVED:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Volunteer account is {user.volunteer.approval_status.value.lower()}."
                )

        token = create_access_token(
            {
                "sub": str(user.id),
                "role": user.role.value
            }
        )

        approval_status = (
            user.volunteer.approval_status.value 
            if user.volunteer else None
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "user_id": user.id,
            "role": user.role.value,
            "approval_status": approval_status,
            "full_name": user.full_name
        }