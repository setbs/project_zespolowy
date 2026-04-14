from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import db_session
from app.models.album import Album
from app.schemas.album import AlbumCreate, AlbumRead

router = APIRouter(prefix="/albums", tags=["albums"])


@router.get("", response_model=list[AlbumRead])
def list_albums(db: Session = Depends(db_session)):
    return db.query(Album).order_by(Album.created_at.desc()).all()


@router.post("", response_model=AlbumRead)
def create_album(payload: AlbumCreate, db: Session = Depends(db_session)):
    album = Album(**payload.model_dump())
    db.add(album)
    db.commit()
    db.refresh(album)
    return album
