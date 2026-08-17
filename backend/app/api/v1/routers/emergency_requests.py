from fastapi import APIRouter, Depends,status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.schemas.emergency_assignment import AcceptEmergencyResponse
from app.db.session import get_db
from app.schemas.emergency_request import SOSRequest, SOSResponse
from app.services.emergency_request_service import EmergencyRequestService

router = APIRouter(
    prefix="/emergencies",
    tags=["Emergencies"],
)

@router.post("/sos", response_model=SOSResponse,status_code=status.HTTP_201_CREATED,)
async def create_sos(
    request: SOSRequest,
    db: AsyncSession = Depends(get_db),
):

    return await EmergencyRequestService.create_sos(
        db=db,
        data=request,
    )
    
@router.post(
    "/{emergency_id}/accept/{volunteer_id}",
    response_model=AcceptEmergencyResponse,
)
async def accept_emergency(
    emergency_id: UUID,
    volunteer_id: UUID,
    db: AsyncSession = Depends(get_db),
):

    return await EmergencyRequestService.accept_emergency(
        db=db,
        emergency_id=emergency_id,
        volunteer_id=volunteer_id,
    )