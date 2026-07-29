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


    # volunteers table
    nrc_number: str = Field(
        min_length=5,
        max_length=30
    )

    address: str

    certificate_url: str | None = None


class LoginRequest(BaseModel):

    phone: str

    password: str

class TokenResponse(BaseModel):

    access_token: str

    token_type: str = "bearer"

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

    user_id: UUID

    role: str

    full_name: str