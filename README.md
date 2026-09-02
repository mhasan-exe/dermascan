# DERMA Research API

FastAPI backend for the DERMA skin-lesion research prototype.

## Architecture

Flutter app → FastAPI → ML inference → PostgreSQL (Neon)

The current backend is deliberately ML-free. It provides the API contract and database layer first so the Flutter client can be developed against stable endpoints.

## Endpoints

- `GET /api/health`
- `GET /api/questions`
- `POST /api/screenings`
- `GET /api/screenings/{id}`
- `GET /docs`

## Local setup

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
uvicorn api.index:app --reload
```

Then open `http://127.0.0.1:8000/docs`.

## Neon

Create a Neon PostgreSQL database and set:

```text
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST/DBNAME?sslmode=require
```

Do not commit `.env`.

## Vercel

Vercel supports FastAPI on its Python runtime. The `api/index.py` entrypoint exposes the FastAPI `app`.

Deploy from the project root:

```bash
npm i -g vercel
vercel
```

Add `DATABASE_URL` in Vercel project Environment Variables, then deploy production:

```bash
vercel --prod
```

## Research safety boundary

This API does not currently generate medical diagnoses, cancer probabilities, or cancer stages. Those outputs must only be implemented after the selected research dataset provides appropriate labels and the model has been trained and evaluated.

The final application should clearly identify itself as a research prototype and not a substitute for professional medical assessment.

## Next milestones

1. Connect Neon and verify CRUD.
2. Add image upload validation.
3. Add dataset preprocessing/training pipeline.
4. Add image-only baseline.
5. Add structured metadata/questionnaire experiment.
6. Add explainability such as Grad-CAM.
7. Only implement any stage-related experiment if the dataset has valid staging labels.
8. Build Flutter client against the stable API.
