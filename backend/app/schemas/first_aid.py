from pydantic import BaseModel


class FirstAidStepResponse(BaseModel):
    id: int
    category_id: int
    step_number: int
    instruction_en: str
    instruction_mm: str


class FirstAidCategoryResponse(BaseModel):
    id: int
    name_en: str
    name_mm: str
    priority: int
    steps: list[FirstAidStepResponse]