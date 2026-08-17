from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class VolunteerRegisterRequest(BaseModel):
    # users table
    full_name: str = Field(
        min_length=2,
        max_length=100
    )
    phone: str = Field(
        min_length=7,
        max_length=20
    )
    email: EmailStr | None = None
    password: str = Field(
        min_length=8
    )
    nrc_number: str = Field(
        min_length=5,
        max_length=30
    )
    address: str
    certificate_url: str | None = None
    latitude: float | None = Field(default=None, ge=-90, le=90)
    longitude: float | None = Field(default=None, ge=-180, le=180)

class LoginRequest(BaseModel):
    phone: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role:str
    approval_status: str | None = None

class UserResponse(BaseModel):
    id: UUID
    full_name: str
    phone: str
    email: str | None
    role: str
    class Config:
        from_attributes = True
        
class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str
    approval_status: str | None = None