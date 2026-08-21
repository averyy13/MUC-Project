from pydantic import BaseModel

class EmergencyContactResponse(BaseModel):
    id: str
    name_en: str
    name_mm: str
    phone: str
    type: str
    latitude: float
    longitude: float
    distance_km: float