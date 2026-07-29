from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.emergency_request import SOSRequest
from app.services.emergency_request_service import EmergencyService

router = APIRouter(
    prefix="/emergencies",
    tags=["Emergencies"],
)


@router.post("/sos")
async def create_sos(
    request: SOSRequest,
    db: AsyncSession = Depends(get_db),
):

    return await EmergencyService.create_sos(
        db,
        request,
    )