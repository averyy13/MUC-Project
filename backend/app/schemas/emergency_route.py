from pydantic import BaseModel

class EmergencyRouteResponse(BaseModel):
    emergency_id: str
    rescue_team_latitude: float
    rescue_team_longitude: float
    requester_latitude: float
    requester_longitude: float
    distance_meters: int
    duration_seconds: int
    encoded_polyline: str
    rescue_team_name: str