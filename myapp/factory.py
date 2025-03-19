import logging
from logging.config import dictConfig

import quart_flask_patch
from quart import Quart
from quart_session import Session
from flask_sqlalchemy import SQLAlchemy

from myapp import config
from myapp import logs


db = SQLAlchemy()

def create_app():
    from myapp import filters
    from myapp.cli import main as cli
    # from myapp.routes import auth
    from myapp.routes import main
    app = Quart(__name__)
    app.config.from_envvar("FLASK_SECRETS", "config.py")
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_TYPE"] = "redis"
    app.config["SESSION_PROTECTION"] = True
    db.init_app(app)
    Session(app)
    app.register_blueprint(cli.bp)
    dictConfig(config.LOGGING_CONFIG)

    if config.LOG_DIRECTORY:
        logs.configure_logging()

    @app.before_serving
    async def startup():
        app.register_blueprint(filters.bp)
        app.register_blueprint(main.bp)
        # app.register_blueprint(auth.bp)

    return app
