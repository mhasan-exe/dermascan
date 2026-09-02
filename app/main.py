from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.health import router as health_router
from app.routes.questions import router as questions_router
from app.routes.screenings import router as screenings_router

app = FastAPI(
    title="DERMA Research API",
    version="0.1.0",
    description="Research prototype API for skin-lesion image analysis and structured questionnaire experiments.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to the Flutter app domain before production.
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api")
app.include_router(questions_router, prefix="/api")
app.include_router(screenings_router, prefix="/api")
