from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import db_session
from app.models.album import Album
from app.models.rating import Rating
from app.schemas.rating import RatingCreate, RatingRead, RatingUpdate

router = APIRouter(prefix="/ratings", tags=["ratings"])


@router.get("", response_model=list[RatingRead])
def list_ratings(db: Session = Depends(db_session)):
    return db.query(Rating).order_by(Rating.created_at.desc()).all()


@router.post("", response_model=RatingRead, status_code=status.HTTP_201_CREATED)
def create_rating(payload: RatingCreate, db: Session = Depends(db_session)):
    album = db.query(Album).filter(Album.id == payload.album_id).first()
    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album not found")

    rating = Rating(album_id=payload.album_id, user_id=1, score=payload.score, review=payload.review)
    db.add(rating)
    db.commit()
    db.refresh(rating)
    return rating


@router.patch("/{rating_id}", response_model=RatingRead)
def update_rating(rating_id: int, payload: RatingUpdate, db: Session = Depends(db_session)):
    rating = db.query(Rating).filter(Rating.id == rating_id).first()
    if not rating:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")

    if payload.score is not None:
        rating.score = payload.score
    if payload.review is not None:
        rating.review = payload.review

    db.commit()
    db.refresh(rating)
    return rating
