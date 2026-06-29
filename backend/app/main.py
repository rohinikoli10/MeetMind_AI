from fastapi import FastAPI
from sqlalchemy import text
from app.routers import chat
from app.database.database import engine
from app.routers.auth import router as auth_router
from app.routers.user import router as user_router
from app.routers.meeting import router as meeting_router

app = FastAPI(
    title="MeetMind AI API",
    description="Backend API for AI Meeting Intelligence Platform",
    version="1.0.0"
)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(meeting_router)
app.include_router(chat.router)
@app.get("/")
def root():
    return {
        "message": "Welcome to MeetMind AI Backend"
    }


@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "success",
            "database": "Connected Successfully"
        }

    except Exception as e:
        return {
            "status": "error",
            "database": str(e)
        }