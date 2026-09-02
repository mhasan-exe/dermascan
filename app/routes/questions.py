from fastapi import APIRouter

router = APIRouter(prefix="/questions", tags=["questionnaire"])

QUESTIONS = [
    {"id": "duration", "text": "How long has the lesion been present?", "type": "single_choice",
     "options": ["Less than 1 month", "1–6 months", "6–12 months", "More than 1 year", "Not sure"]},
    {"id": "change", "text": "Has it changed in size, shape, or color?", "type": "single_choice",
     "options": ["Yes", "No", "Not sure"]},
    {"id": "itching", "text": "Has it been itchy or irritated?", "type": "single_choice",
     "options": ["Yes", "No", "Not sure"]},
    {"id": "bleeding", "text": "Has it bled or formed a persistent sore?", "type": "single_choice",
     "options": ["Yes", "No", "Not sure"]},
    {"id": "pain", "text": "Has it been painful or tender?", "type": "single_choice",
     "options": ["Yes", "No", "Not sure"]},
    {"id": "location", "text": "Where is the lesion located?", "type": "single_choice",
     "options": ["Face/head", "Torso", "Arms/hands", "Legs/feet", "Other"]},
]


@router.get("")
def get_questions():
    return {"questions": QUESTIONS}
