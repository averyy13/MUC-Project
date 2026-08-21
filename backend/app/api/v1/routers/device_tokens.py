from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.user import User
from app.models.volunteer import Volunteer  # <-- Ensure this import matches your project
from app.schemas.device_token import (
    DeviceTokenRegisterRequest,
    DeviceTokenResponse,
)
from app.services.device_token_service import (
    DeviceTokenService,
)
from app.core.dependencies import require_volunteer


router = APIRouter(
    prefix="/volunteers/me",
    tags=["Volunteer Device Tokens"],
)


@router.post(
    "/device-token",
    response_model=DeviceTokenResponse,
)
async def register_device_token(
    data: DeviceTokenRegisterRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):

    # 1. Asynchronously fetch the volunteer record connected to this user
    result = await db.execute(
        select(Volunteer).where(Volunteer.user_id == current_user.id)
    )
    volunteer = result.scalar_one_or_none()

    if volunteer is None:
        raise HTTPException(
            status_code=404,
            detail="Volunteer profile not found",
        )

    # 2. Pass the explicitly fetched volunteer.id
    return await DeviceTokenService.register_token(
        db=db,
        volunteer_id=volunteer.id,
        data=data,
    )