from pydantic import BaseModel, ConfigDict


class EmergencyCategoryResponse(BaseModel):
    id: int
    name_en: str
    name_mm: str
    priority: int

    model_config = ConfigDict(from_attributes=True)