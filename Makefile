setup:
	uv sync

shell:
	FLASK_SECRETS=config.py QUART_APP="app.factory:create_app()" uv run quart shell

dbshell:
	docker-compose exec database psql -U myapp

dev:
	uv run alembic upgrade head
	FLASK_SECRETS=config.py QUART_APP="app.factory:create_app()" uv run quart run

prod:
	FLASK_SECRETS=config.py QUART_APP="app.factory:create_app()" .uv run uvicorn app:app --host 0.0.0.0 --port 5000

up:
	docker-compose up -d

down:
	docker-compose down
