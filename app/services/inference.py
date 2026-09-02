from dataclasses import dataclass


@dataclass
class InferenceResult:
    lesion_category: str | None
    confidence: float | None
    stage_prediction: str | None
    model_version: str


def predict(image_bytes: bytes, questionnaire: dict) -> InferenceResult:
    # Placeholder for the trained model.
    # Never return invented medical predictions.
    return InferenceResult(
        lesion_category=None,
        confidence=None,
        stage_prediction=None,
        model_version="unloaded",
    )
