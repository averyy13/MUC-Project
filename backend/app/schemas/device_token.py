from pydantic import BaseModel, Field


class DeviceTokenRegisterRequest(BaseModel):
    fcm_token: str = Field(..., min_length=1)
    platform: str = Field(default="ANDROID")


class DeviceTokenResponse(BaseModel):
    message: str
    
class DeviceTokenDeleteRequest(BaseModel):
    fcm_token: str