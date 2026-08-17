from uuid import UUID

from pydantic import BaseModel, ConfigDict


class NearbyFacilityResponse(BaseModel):
    id: UUID

    name_en: str
    name_mm: str

    phone: str | None = None

    address_en: str | None = None
    address_mm: str | None = None

    type: str

    latitude: float
    longitude: float

    distance_km: float

    model_config = ConfigDict(from_attributes=True)