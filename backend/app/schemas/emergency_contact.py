from pydantic import BaseModel
from uuid import UUID
from pydantic import BaseModel

class RescueRouteResponse(BaseModel):
    contact_id: UUID
    user_latitude: float
    user_longitude: float
    contact_latitude: float
    contact_longitude: float
    distance_meters: int
    duration_seconds: int
    encoded_polyline: str
    
class EmergencyContactResponse(BaseModel):
    id: str
    name_en: str
    name_mm: str
    phone: str
    type: str
    latitude: float
    longitude: float
    distance_km: float