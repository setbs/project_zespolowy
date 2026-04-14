from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.db.session import Base, engine
from app.models import album, rating, user  # noqa: F401

settings = get_settings()
app = FastAPI(title=settings.project_name)
app.include_router(api_router, prefix=settings.api_v1_str)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "MusicRate API"}
