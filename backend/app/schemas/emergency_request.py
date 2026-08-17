from uuid import UUID
from pydantic import BaseModel, Field
class SOSRequest(BaseModel):
    category_id: int
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    description: str | None = None

class RescueContactResponse(BaseModel):
    id: UUID
    name_en: str
    phone: str
    type: str
    latitude: float
    longitude: float
    distance_meters: float
    
class SOSResponse(BaseModel):
    emergency_id: UUID
    notified_volunteers: int
    nearest_rescue_contact: RescueContactResponse
    medical_facilities: list