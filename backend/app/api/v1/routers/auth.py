from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.auth import VolunteerRegisterRequest
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register-volunteer")
async def register_volunteer(
    data: VolunteerRegisterRequest,
    db: AsyncSession = Depends(get_db)
):

    return await AuthService.register_volunteer(
        db,
        data
    )
    
@router.post("/login")
async def login(
    data: LoginRequest,
    db: AsyncSession = Depends(get_db)

):
    return await AuthService.login(
        db,
        data
    )
    
@router.get("/me")
async def me(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "name": current_user.full_name,
        "phone": current_user.phone,
        "role": current_user.role.value
    }