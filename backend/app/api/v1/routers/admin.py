from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.services.admin_service import AdminService
from app.core.dependencies import require_admin
from app.models.user import User

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/pending-volunteers")
async def pending_volunteers(
    db: AsyncSession = Depends(get_db)
):

    return await AdminService.list_pending(db)


@router.patch("/approve/{volunteer_id}")
async def approve(
    volunteer_id: UUID,
    db: AsyncSession = Depends(get_db),
    admin: User = Depends(require_admin)
):
    return await AdminService.approve(
        db,
        volunteer_id
    )