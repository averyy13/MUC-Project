import uuid
from fastapi import APIRouter, Depends, status, WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.schemas.emergency_assignment import AcceptEmergencyResponse
from app.db.session import get_db, AsyncSessionLocal
from app.schemas.emergency_request import EmergencyStatusResponse, SOSRequest, SOSResponse, EmergencyActionResponse
from app.services.emergency_request_service import EmergencyRequestService
from app.core.dependencies import require_volunteer
from app.models.user import User
from app.core.security import decode_access_token
from app.repositories.auth_repository import AuthRepository
from app.repositories.volunteer_assignment_repository import VolunteerAssignmentRepository
from app.repositories.volunteer_repository import VolunteerRepository
from app.services.emergency_tracking_service import tracking_manager
from app.models.enums import AssignmentStatus, EmergencyStatus
from app.models.emergency_request import EmergencyRequest
from app.schemas.emergency_tracking import VolunteerLocationMessage

router = APIRouter(
    prefix="/emergencies",
    tags=["Emergencies"],
)

@router.post("/sos", response_model=SOSResponse, status_code=status.HTTP_201_CREATED)
async def create_sos(
    request: SOSRequest,
    db: AsyncSession = Depends(get_db),
):
    return await EmergencyRequestService.create_sos(
        db=db,
        data=request,
    )

@router.get("/{emergency_id}", response_model=EmergencyStatusResponse)
async def get_emergency_status(
    emergency_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await EmergencyRequestService.get_emergency_status(
        db=db,
        emergency_id=emergency_id,
    )   

@router.post("/{emergency_id}/accept", response_model=AcceptEmergencyResponse)
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
    
@router.post("/{emergency_id}/en-route")
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
    
@router.get("/{emergency_id}/route")
async def get_emergency_route(
    emergency_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await EmergencyRequestService.get_emergency_route(
        db=db,
        emergency_id=emergency_id,
    )
    
@router.post("/{emergency_id}/arrived")
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

@router.post("/{emergency_id}/complete")
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
    
@router.post("/{emergency_id}/cancel", response_model=EmergencyActionResponse)
async def cancel_emergency(
    emergency_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await EmergencyRequestService.cancel_emergency(
        db=db,
        emergency_id=emergency_id,
    )


# ---------------------------------------------------------
# VOLUNTEER TRACKING WEBSOCKET
# ---------------------------------------------------------
@router.websocket("/{emergency_id}/tracking/volunteer")
async def volunteer_tracking_websocket(
    websocket: WebSocket,
    emergency_id: UUID,
):
    """
    Volunteer WebSocket.
    Volunteer:
        - authenticates with JWT
        - sends GPS location
        - server persists location
        - server broadcasts location to requester
    """

    # 1. Authenticate volunteer
    authorization = websocket.headers.get("authorization")

    if not authorization or not authorization.lower().startswith("bearer "):
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    token = authorization.split(" ", 1)[1]
    payload = decode_access_token(token)

    if payload is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    user_id = payload.get("sub")

    if not user_id:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    # 2. Get user + volunteer
    async with AsyncSessionLocal() as db:
        user = await AuthRepository.get_user_by_id(db, user_id)

        if user is None:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        volunteer = await VolunteerRepository.get_by_user_id(db, user.id)

        if volunteer is None:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        # 3. Get emergency
        emergency = await db.get(EmergencyRequest, emergency_id)

        if emergency is None:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        # 4. Verify assigned volunteer
        if emergency.assigned_volunteer_id != volunteer.id:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        # 5. Verify assignment
        assignment = await VolunteerAssignmentRepository.get_for_request_and_volunteer(
            db,
            emergency_id,
            volunteer.id,
        )

        if assignment is None:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        if assignment.status != AssignmentStatus.ACCEPTED:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        # 6. Verify emergency status
        if emergency.status != EmergencyStatus.VOLUNTEER_EN_ROUTE:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        # 7. Accept connection
        await websocket.accept()

        try:
            while True:
                # Receive GPS location
                raw_message = await websocket.receive_json()

                try:
                    message = VolunteerLocationMessage.model_validate(raw_message)
                except Exception:
                    await websocket.send_json({
                        "type": "ERROR",
                        "message": "Invalid location data",
                    })
                    continue

                if message.type != "VOLUNTEER_LOCATION":
                    continue

                # Use a fresh DB session for each GPS update
                async with AsyncSessionLocal() as location_db:
                    current_emergency = await location_db.get(EmergencyRequest, emergency_id)

                    if current_emergency is None:
                        break

                    # Stop tracking after the rescue state changes
                    if current_emergency.status != EmergencyStatus.VOLUNTEER_EN_ROUTE:
                        break

                    current_assignment = await VolunteerAssignmentRepository.get_for_request_and_volunteer(
                        location_db,
                        emergency_id,
                        volunteer.id,
                    )

                    if current_assignment is None:
                        break

                    if current_assignment.status != AssignmentStatus.ACCEPTED:
                        break

                    # Save latest location
                    await VolunteerRepository.update_current_location(
                        db=location_db,
                        volunteer_id=volunteer.id,
                        latitude=message.latitude,
                        longitude=message.longitude,
                        speed=message.speed,
                        heading=message.heading,
                    )
                    await location_db.commit()

                # Broadcast to requester
                await tracking_manager.broadcast_location(
                    str(emergency_id),
                    {
                        "type": "VOLUNTEER_LOCATION",
                        "emergency_id": str(emergency_id),
                        "volunteer_id": str(volunteer.id),
                        "latitude": message.latitude,
                        "longitude": message.longitude,
                        "speed": message.speed,
                        "heading": message.heading,
                    }
                )

        except WebSocketDisconnect:
            pass
        except Exception:
            try:
                await websocket.close(code=status.WS_1011_INTERNAL_ERROR)
            except Exception:
                pass


# ---------------------------------------------------------
# REQUESTER TRACKING WEBSOCKET
# ---------------------------------------------------------
@router.websocket("/{emergency_id}/tracking/requester")
async def requester_tracking_websocket(
    websocket: WebSocket,
    emergency_id: UUID,
):
    """
    Requester WebSocket.
    Requester:
        - authenticates using X-Device-ID
        - receives volunteer GPS updates
        - cannot send location
    """

    device_id_header = websocket.headers.get("x-device-id")

    if not device_id_header:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    try:
        device_id = uuid.UUID(device_id_header)
    except ValueError:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    async with AsyncSessionLocal() as db:
        # 1. Get emergency
        emergency = await db.get(EmergencyRequest, emergency_id)

        if emergency is None:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        # 2. Verify requester owns this emergency
        if emergency.device_id != device_id:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        # 3. Only allow active emergencies
        if emergency.status in (EmergencyStatus.COMPLETED, EmergencyStatus.CANCELLED):
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        # 4. Register requester connection
        await tracking_manager.connect_requester(str(emergency_id), websocket)

        try:
            while True:
                # Requester does not send messages. We wait here so the connection stays alive and can detect disconnects.
                # It accepts harmless pings if sent.
                await websocket.receive_text()

        except WebSocketDisconnect:
            pass
        finally:
            tracking_manager.disconnect_requester(str(emergency_id), websocket)