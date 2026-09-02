from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import Base, engine, get_db
from app.models.screening import Screening
from app.schemas.screening import ScreeningCreate, ScreeningResponse

router = APIRouter(prefix="/screenings", tags=["screenings"])

# Creates tables for the first prototype deployment.
# Later this should be replaced with Alembic migrations.
Base.metadata.create_all(bind=engine)


@router.post("", response_model=ScreeningResponse)
def create_screening(payload: ScreeningCreate, db: Session = Depends(get_db)):
    # ML inference is intentionally not faked here.
    # The real model service will populate these fields after integration.
    screening = Screening(
        image_filename=payload.image_filename,
        questionnaire_data=payload.questionnaire_data,
        lesion_category=None,
        prediction_confidence=None,
        stage_prediction=None,
        model_version="unloaded",
        explanation="No ML model is loaded yet. This record stores the research-session input only.",
    )
    db.add(screening)
    db.commit()
    db.refresh(screening)
    return screening


@router.get("/{screening_id}", response_model=ScreeningResponse)
def get_screening(screening_id: int, db: Session = Depends(get_db)):
    screening = db.get(Screening, screening_id)
    if screening is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Screening not found")
    return screening
