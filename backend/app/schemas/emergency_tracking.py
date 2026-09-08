from pydantic import BaseModel, Field
class VolunteerLocationMessage(BaseModel):
    type: str
    latitude: float = Field(
        ge=-90,
        le=90
    )
    longitude: float = Field(
        ge=-180,
        le=180
    )
    speed: float | None = None
    heading: float | None = None