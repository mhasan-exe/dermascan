from datetime import datetime
from pydantic import BaseModel, Field


class ScreeningCreate(BaseModel):
    image_filename: str | None = Field(default=None, max_length=255)
    questionnaire_data: dict[str, object] = Field(default_factory=dict)


class ScreeningResponse(BaseModel):
    id: int
    created_at: datetime
    lesion_category: str | None
    prediction_confidence: float | None
    stage_prediction: str | None
    questionnaire_data: dict | None
    model_version: str
    explanation: str | None

    model_config = {"from_attributes": True}
