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
    
class FacilityRouteResponse(BaseModel):
    facility_id: UUID
    user_latitude: float
    user_longitude: float
    facility_latitude: float
    facility_longitude: float
    distance_meters: int
    duration_seconds: int
    encoded_polyline: str