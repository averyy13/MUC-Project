from uuid import UUID

from pydantic import BaseModel, Field


class SOSRequest(BaseModel):
    category_id: UUID
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    description: str | None = None


class SOSResponse(BaseModel):
    emergency_id: UUID
    matched_volunteers: list
    rescue_contacts: list
    medical_facilities: list