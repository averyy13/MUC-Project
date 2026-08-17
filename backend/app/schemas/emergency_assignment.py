from uuid import UUID
from pydantic import BaseModel

class AcceptEmergencyResponse(BaseModel):
    emergency_id: UUID
    volunteer_id: UUID
    status: str
    message: str