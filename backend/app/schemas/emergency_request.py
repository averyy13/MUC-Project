from uuid import UUID
from pydantic import BaseModel, Field
class SOSRequest(BaseModel):
    category_id: int
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    description: str | None = None
    device_id: UUID | None = None

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
class AssignedVolunteerLocationResponse(BaseModel):
    latitude: float
    longitude: float
    speed: float | None = None
    heading: float | None = None


class AssignedVolunteerResponse(BaseModel):
    id: UUID
    name: str
    phone: str
    assignment_status: str | None = None
    location: AssignedVolunteerLocationResponse | None = None


class EmergencyStatusResponse(BaseModel):
    emergency_id: UUID
    status: str
    assignment_status: str | None = None    
    category_id: int
    category_name_en: str
    category_name_mm: str
    description: str | None = None
    latitude: float
    longitude: float
    distance_meters: float | None = None
    assigned_volunteer: AssignedVolunteerResponse | None = None
    created_at: str | None = None
    updated_at: str | None = None
    notified_at: str | None = None
    accepted_at: str | None = None
    arrived_at: str | None = None
    completed_at: str | None = None
    location_updated_at: str | None = None
    
class EmergencyActionResponse(BaseModel):
    emergency_id: UUID
    status: str
    message: str