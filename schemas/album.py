from pydantic import BaseModel, Field


class AlbumBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    artist: str = Field(min_length=1, max_length=255)
    genre: str | None = Field(default=None, max_length=100)
    year: int | None = Field(default=None, ge=1900, le=2100)
    cover_url: str | None = Field(default=None, max_length=500)


class AlbumCreate(AlbumBase):
    pass


class AlbumRead(AlbumBase):
    id: int
    avg_rating: float

    model_config = {"from_attributes": True}
