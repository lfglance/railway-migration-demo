# railway migration demo

This application is for learning the Railway platform, simulating a migration from AWS to Railway.

The demo application is backend API which is used by a mobile application. It consists of the following technologies:
* Quart API (Python, async Flask)
* PostgreSQL DB
* Redis cache
* Background worker

# railway setup

This is the runbook to deploy the system on Railway.

```bash
alias rw="railway"

# Create new project
rw init -n lance-rw-demo

# Link project to CLI
rw link -p lance-rw-demo -t "lance's Projects"

# Add PostgreSQL service
rw add -d postgres -s postgres

# Add Redis service
rw add -d redis -s redis

# Add empty service for rps app
rw add -s rps-api

# Create domain for app service
rw domain

# Load environment variables for app
python load_envs.py
```

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
