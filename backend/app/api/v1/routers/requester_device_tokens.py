from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.requester_device_token import (
    RequesterDeviceTokenRegisterRequest,
    RequesterDeviceTokenResponse,
)
from app.services.requester_device_token_service import (
    RequesterDeviceTokenService,
)


router = APIRouter(
    prefix="/requesters",
    tags=["Requester Device Tokens"],
)


@router.post(
    "/device-token",
    response_model=RequesterDeviceTokenResponse,
)
async def register_requester_device_token(
    data: RequesterDeviceTokenRegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    return await RequesterDeviceTokenService.register_token(
        db=db,
        device_id=data.device_id,
        fcm_token=data.fcm_token,
        platform=data.platform,
    )