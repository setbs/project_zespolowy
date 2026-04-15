from dataclasses import dataclass

import httpx

from app.core.config import get_settings


@dataclass
class LastFmResult:
    payload: dict
    source: str = "lastfm"


class LastFmClient:
    def __init__(self) -> None:
        settings = get_settings()
        self.api_key = settings.lastfm_api_key
        self.base_url = settings.lastfm_base_url

    async def search_album(self, query: str) -> LastFmResult:
        params = {
            "method": "album.search",
            "album": query,
            "api_key": self.api_key,
            "format": "json",
        }
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(self.base_url, params=params)
            response.raise_for_status()
            return LastFmResult(payload=response.json())

    async def search_artist(self, query: str) -> LastFmResult:
        params = {
            "method": "artist.search",
            "artist": query,
            "api_key": self.api_key,
            "format": "json",
        }
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(self.base_url, params=params)
            response.raise_for_status()
            return LastFmResult(payload=response.json())
