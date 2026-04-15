from pydantic import BaseModel, Field


class RatingCreate(BaseModel):
    album_id: int
    score: int = Field(ge=1, le=10)
    review: str | None = Field(default=None, max_length=1000)


class RatingUpdate(BaseModel):
    score: int | None = Field(default=None, ge=1, le=10)
    review: str | None = Field(default=None, max_length=1000)


class RatingRead(BaseModel):
    id: int
    user_id: int
    album_id: int
    score: int
    review: str | None

    model_config = {"from_attributes": True}
