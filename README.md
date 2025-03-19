# quart-template

This is my preferred template for new web dev projects using Quart, Alembic, Redis, and Postgres.

```bash
# install dependencies
uv sync  # make setup

# start postgres/redis
docker compose up -d  # make up

# generate db migrations
uv run alembic revision --autogenerate -m "describe schema change"

# run migrations
uv run alembic upgrade head  # make dev

# run dev web server
uv run quart run  # make dev
```
