# railway migration demo

This application is for learning the Railway platform, simulating a migration from AWS to Railway.

The demo application is backend API which is used by a mobile application. It consists of the following technologies:
* Quart API (Python, async Flask)
* PostgreSQL DB
* Redis cache
* Background worker

# local app setup

Prepare the local application to simulate a production environment on AWS.

```bash
# Install python dependencies
uv sync

# Bring up local containers (postgres, redis)
docker-compose up -d

# Apply db migrations
uv run alembic upgrade head

# Start development server
FLASK_SECRETS=config.py QUART_APP="rps.factory:create_app()" uv run quart --debug run

# Load dummy data
uv run python simulate.py
```

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
rw add -s rps-api -v DEMO=1
rw add -s rps-worker -v DEMO=1

# Copy sample env file
cp rw.example.env rw.env

# Load environment variables for app
python load_envs.py

# Create domain for app service with required port
rw domain -s rps-api -p 8000 # cli bug, fix port

# Specify railway.toml and deploy application
cp railway.api.toml railway.toml
rw up -d -s rps-api

cp railway.worker.toml railway.toml
rw up -d -s rps-worker

cp railway.api.toml railway.toml
```

# data migration

```bash
# Create database export folder
mkdir -p data

# Dump database
docker-compose exec database pg_dump -U rps -d rps > data/dump.sql

# Halt writes to source database
docker-compose exec database psql -U rps -d rps -f halt_writes.sql

# Import variables for Postgres service into terminal session
export $(rw variables -s Postgres -k)

# Drop existing tables
psql -h ${RAILWAY_TCP_PROXY_DOMAIN} -p ${RAILWAY_TCP_PROXY_PORT} -U ${PGUSER} -d ${PGDATABASE} -f drop_tables.sql

# Perform restore
psql -h ${RAILWAY_TCP_PROXY_DOMAIN} -p ${RAILWAY_TCP_PROXY_PORT} -U ${PGUSER} -d ${PGDATABASE} -f data/dump.sql

# Repeat above steps as needed
```

# production requirements

* cost projections
* platform security + 2fa
* CI/CD
* lower environments
* multi-region, HA
* observability
* centralized logging + notification
* private VPN
* backups