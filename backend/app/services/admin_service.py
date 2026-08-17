from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.enums import ApprovalStatus
from app.repositories.admin_repository import AdminRepository

class AdminService:
    @staticmethod
    async def list_pending(db: AsyncSession):
        volunteers = await AdminRepository.get_volunteers_by_status(
            db,
            ApprovalStatus.PENDING,
        )
        return [
            {
                "volunteer_id": str(v.id),
                "full_name": v.user.full_name,
                "phone": v.user.phone,
                "email": v.user.email,
                "nrc_number": v.nrc_number,
                "address": v.address,
                "approval_status": v.approval_status.value,
                "created_at": v.created_at,
            }
            for v in volunteers
        ]

    @staticmethod
    async def list_approved(db: AsyncSession):
        volunteers = await AdminRepository.get_volunteers_by_status(
            db,
            ApprovalStatus.APPROVED,
        )
        return [
            {
                "volunteer_id": str(v.id),
                "full_name": v.user.full_name,
                "phone": v.user.phone,
                "email": v.user.email,
                "availability": v.availability,
                "approval_status": v.approval_status.value,
            }
            for v in volunteers
        ]

    @staticmethod
    async def list_rejected(db: AsyncSession):
        volunteers = await AdminRepository.get_volunteers_by_status(
            db,
            ApprovalStatus.REJECTED,
        )
        return [
            {
                "volunteer_id": str(v.id),
                "full_name": v.user.full_name,
                "phone": v.user.phone,
                "email": v.user.email,
                "approval_status": v.approval_status.value,
            }
            for v in volunteers
        ]

    @staticmethod
    async def approve(db: AsyncSession, volunteer_id):
        volunteer = await AdminRepository.get_volunteer(db, volunteer_id)

        if volunteer is None:
            raise HTTPException(404, "Volunteer not found")

        await AdminRepository.update_status(
            db,
            volunteer,
            ApprovalStatus.APPROVED,
        )

        await db.commit()

        return {
            "volunteer_id": str(volunteer.id),
            "full_name": volunteer.user.full_name,
            "phone": volunteer.user.phone,
            "approval_status": volunteer.approval_status.value,
        }

    @staticmethod
    async def reject(db: AsyncSession, volunteer_id):
        volunteer = await AdminRepository.get_volunteer(db, volunteer_id)

        if volunteer is None:
            raise HTTPException(404, "Volunteer not found")

        await AdminRepository.update_status(
            db,
            volunteer,
            ApprovalStatus.REJECTED,
        )

        await db.commit()

        return {
            "volunteer_id": str(volunteer.id),
            "full_name": volunteer.user.full_name,
            "phone": volunteer.user.phone,
            "approval_status": volunteer.approval_status.value,
        }