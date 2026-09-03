from fastapi import APIRouter, Depends,status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.schemas.emergency_assignment import AcceptEmergencyResponse
from app.db.session import get_db
from app.schemas.emergency_request import EmergencyStatusResponse, SOSRequest, SOSResponse, EmergencyActionResponse
from app.services.emergency_request_service import EmergencyRequestService
from app.core.dependencies import require_volunteer
from app.models.user import User

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
@router.get(
    "/{emergency_id}",
    response_model=EmergencyStatusResponse,
)
async def get_emergency_status(
    emergency_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await EmergencyRequestService.get_emergency_status(
        db=db,
        emergency_id=emergency_id,
    )   
@router.post(
    "/{emergency_id}/accept",
    response_model=AcceptEmergencyResponse,
)
async def accept_emergency(
    emergency_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):
    return await EmergencyRequestService.accept_emergency(
        db=db,
        emergency_id=emergency_id,
        user_id=current_user.id, 
    )
    
@router.post( "/{emergency_id}/en-route",)
async def start_rescue(
    emergency_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):
    return await EmergencyRequestService.start_rescue(
        db=db,
        emergency_id=emergency_id,
        user_id=current_user.id,
    )
    
@router.get("/{emergency_id}/route",)
async def get_emergency_route(
    emergency_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await EmergencyRequestService.get_emergency_route(
        db=db,
        emergency_id=emergency_id,
    )
    
@router.post( "/{emergency_id}/arrived",)
async def mark_arrived(
    emergency_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):
    return await EmergencyRequestService.mark_arrived(
        db=db,
        emergency_id=emergency_id,
        user_id=current_user.id,
    )

@router.post( "/{emergency_id}/complete",)
async def complete_rescue(
    emergency_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_volunteer),
):
    return await EmergencyRequestService.complete_rescue(
        db=db,
        emergency_id=emergency_id,
        user_id=current_user.id,
    )
    
@router.post(
    "/{emergency_id}/cancel",
    response_model=EmergencyActionResponse,
)
async def cancel_emergency(
    emergency_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await EmergencyRequestService.cancel_emergency(
        db=db,
        emergency_id=emergency_id,
    )