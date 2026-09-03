from uuid import UUID

from pydantic import BaseModel


class RequesterDeviceTokenRegisterRequest(BaseModel):
    device_id: UUID
    fcm_token: str
    platform: str = "ANDROID"


class RequesterDeviceTokenResponse(BaseModel):
    device_id: UUID
    message: str