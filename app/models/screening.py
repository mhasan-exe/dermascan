from datetime import datetime
from sqlalchemy import DateTime, Float, Integer, JSON, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Screening(Base):
    __tablename__ = "screenings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    image_filename: Mapped[str | None] = mapped_column(String(255), nullable=True)
    lesion_category: Mapped[str | None] = mapped_column(String(100), nullable=True)
    prediction_confidence: Mapped[float | None] = mapped_column(Float, nullable=True)
    stage_prediction: Mapped[str | None] = mapped_column(String(100), nullable=True)
    questionnaire_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    model_version: Mapped[str] = mapped_column(String(100), default="unloaded")
    explanation: Mapped[str | None] = mapped_column(Text, nullable=True)
