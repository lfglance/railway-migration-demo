setup:
	uv sync

shell:
	FLASK_SECRETS=config.py QUART_APP="rps.factory:create_app()" uv run quart shell

dbshell:
	docker-compose exec database psql -U rps

dev:
	uv run alembic upgrade head
	FLASK_SECRETS=config.py QUART_APP="rps.factory:create_app()" uv run quart --debug run

prod:
	FLASK_SECRETS=config.py QUART_APP="rps.factory:create_app()" uv run uvicorn app:create_app --host 0.0.0.0 --port 8000

up:
	docker-compose up -d

down:
	docker-compose down
