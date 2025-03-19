import logging
from logging.config import dictConfig

import quart_flask_patch
from quart import Quart
from flask_sqlalchemy import SQLAlchemy

from rps import config
from rps import logs


db = SQLAlchemy()

def create_app():
    from rps.routes import auth, system, game
    app = Quart(__name__)
    app.config.from_envvar("FLASK_SECRETS", "config.py")
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    dictConfig(config.LOGGING_CONFIG)

    if config.LOG_DIRECTORY:
        logs.configure_logging()

    @app.before_serving
    async def startup():
        app.register_blueprint(system.bp)
        app.register_blueprint(auth.bp)
        app.register_blueprint(game.bp)

    return app
