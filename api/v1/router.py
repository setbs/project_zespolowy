from fastapi import APIRouter

from app.api.v1.endpoints import albums, auth, health, lastfm, ratings

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(albums.router)
api_router.include_router(ratings.router)
api_router.include_router(lastfm.router)
