from uuid import UUID
from pydantic import BaseModel

class VolunteerApprovalResponse(BaseModel):
    volunteer_id: UUID
    full_name: str
    phone: str
    approval_status: str


class VolunteerListItem(BaseModel):
    volunteer_id: UUID
    user_id: UUID
    full_name: str
    phone: str
    email: str | None
    approval_status: str
    availability: bool

    class Config:
        from_attributes = True

class MedicalFacilityUpdate(BaseModel):
    name_en: str | None = None
    name_mm: str | None = None
    phone: str | None = None
    address_en: str | None = None
    address_mm: str | None = None
    type: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    is_active: bool | None = None

class EmergencyContactUpdate(BaseModel):
    name_en: str | None = None
    name_mm: str | None = None
    phone: str | None = None
    type: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    is_active: bool | None = None