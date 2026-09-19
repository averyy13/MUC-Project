from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RescueHistoryResponse(BaseModel):
    emergency_id: UUID

    category_id: int
    category_name_en: str
    category_name_mm: str

    description: str | None = None

    latitude: float
    longitude: float

    completed_at: datetime

    model_config = ConfigDict(from_attributes=True)