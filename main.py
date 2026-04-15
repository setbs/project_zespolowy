from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.db.session import Base, engine
from app.models import album, rating, user  # noqa: F401
from app.models.album import Album
from app.db.session import SessionLocal
from app.web import frontend_page

settings = get_settings()
app = FastAPI(title=settings.project_name)
app.include_router(api_router, prefix=settings.api_v1_str)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Album).count() == 0:
            db.add_all(
                [
                    Album(title="In Rainbows", artist="Radiohead", genre="Alternative", year=2007),
                    Album(title="To Pimp a Butterfly", artist="Kendrick Lamar", genre="Hip-Hop", year=2015),
                    Album(title="Random Access Memories", artist="Daft Punk", genre="Electronic", year=2013),
                ]
            )
            db.commit()
    finally:
        db.close()


@app.get("/")
def root():
    return frontend_page()
