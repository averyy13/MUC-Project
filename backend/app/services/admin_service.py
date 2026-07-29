from fastapi import HTTPException

from app.models.enums import ApprovalStatus

from app.repositories.admin_repository import AdminRepository


class AdminService:

    @staticmethod
    async def list_pending(db):

        return await AdminRepository.get_volunteers_by_status(
            db,
            ApprovalStatus.PENDING
        )


    @staticmethod
    async def approve(db, volunteer_id):

        volunteer = await AdminRepository.get_volunteer(
            db,
            volunteer_id
        )

        if volunteer is None:
            raise HTTPException(
                404,
                "Volunteer not found"
            )

        volunteer.approval_status = ApprovalStatus.APPROVED

        await db.commit()

        await db.refresh(volunteer)

        return {
            "volunteer_id": volunteer.id,
            "full_name": volunteer.user.full_name,
            "phone": volunteer.user.phone,
            "approval_status": volunteer.approval_status.value
        }