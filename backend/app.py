from fastapi import FastAPI
from api.analyze import router as analyze_router

app = FastAPI(title="Resume Analyzer API")

app.include_router(analyze_router, prefix="/analyze")

@app.get("/")
def root():
    return {"status": "Resume Analyzer Backend Running"}
