from uuid import UUID
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import require_admin
from app.db.session import get_db
from app.models.user import User
from app.services.admin_service import AdminService

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)

@router.get("/pending-volunteers")
async def pending_volunteers(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return await AdminService.list_pending(db)

@router.get("/approved-volunteers")
async def approved_volunteers(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return await AdminService.list_approved(db)

@router.get("/rejected-volunteers")
async def rejected_volunteers(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return await AdminService.list_rejected(db)

@router.patch("/approve/{volunteer_id}")
async def approve_volunteer(
    volunteer_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return await AdminService.approve(db, volunteer_id)

@router.patch("/reject/{volunteer_id}")
async def reject_volunteer(
    volunteer_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return await AdminService.reject(db, volunteer_id)

@router.get("/dashboard-stats")
async def dashboard_stats(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return await AdminService.get_dashboard_stats(db)

@router.get("/emergencies")
async def list_emergencies(
    status: str | None = Query(default=None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return await AdminService.list_emergencies(db, status)

@router.get("/facilities")
async def list_facilities(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return await AdminService.list_facilities(db)

@router.get("/emergency-contacts")
async def list_emergency_contacts(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return await AdminService.list_emergency_contacts(db)