from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "MusicRate"
    api_v1_str: str = "/api/v1"
    secret_key: str = "change-me"
    access_token_expire_minutes: int = 30
    database_url: str = "sqlite:///./dev.db"
    lastfm_api_key: str = "change-me"
    lastfm_base_url: str = "https://ws.audioscrobbler.com/2.0/"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)


@lru_cache
def get_settings() -> Settings:
    return Settings()
