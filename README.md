# MusicRate

Web application for rating music albums and tracking reviews, inspired by RateYourMusic.

## Stack

- Backend: FastAPI
- Database: PostgreSQL
- Auth: JWT-based login flow
- External API: Last.fm

## Implemented scaffold

- FastAPI application entry point
- User, album, and rating models
- Basic auth endpoints for register and login
- Album and rating endpoints
- Last.fm proxy endpoints
- PostgreSQL docker-compose file

## Project structure

- `app/main.py` - FastAPI application bootstrap
- `app/core/` - configuration and security helpers
- `app/db/` - database base and session setup
- `app/models/` - SQLAlchemy models
- `app/schemas/` - Pydantic request/response schemas
- `app/api/v1/endpoints/` - route modules
- `app/services/` - external API clients

## Run locally

1. Copy `.env.example` to `.env`.
2. Install dependencies from `requirements.txt`.
3. Start PostgreSQL with `docker compose up -d`.
4. Run the API with `uvicorn app.main:app --reload`.

## Next steps

1. Add JWT dependency and protected `/auth/me`.
2. Add Alembic migrations.
3. Add album/rating CRUD tied to the authenticated user.
4. Add frontend web app.
