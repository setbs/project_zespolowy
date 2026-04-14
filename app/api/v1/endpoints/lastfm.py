from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse

from app.services.lastfm import LastFmClient

router = APIRouter(prefix="/lastfm", tags=["lastfm"])
client = LastFmClient()


@router.get("/search/album")
async def search_album(q: str = Query(..., min_length=1)):
    try:
        result = await client.search_album(q)
        return JSONResponse(content=result.payload)
    except Exception as exc:  # temporary scaffold; narrow errors next
        raise HTTPException(status_code=502, detail=f"Last.fm error: {exc}") from exc


@router.get("/search/artist")
async def search_artist(q: str = Query(..., min_length=1)):
    try:
        result = await client.search_artist(q)
        return JSONResponse(content=result.payload)
    except Exception as exc:  # temporary scaffold; narrow errors next
        raise HTTPException(status_code=502, detail=f"Last.fm error: {exc}") from exc
