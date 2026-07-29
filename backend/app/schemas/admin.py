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