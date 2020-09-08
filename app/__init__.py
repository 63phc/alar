import os
import pathlib

from flask import Flask
from flask_login import LoginManager
from werkzeug.middleware.proxy_fix import ProxyFix

from app.api import rest_api
from app.api import HelloWorld
from app.db import db, migrate
from app.db.models import User
from app import api as simple_api


def create_app(config=None):
    # init app itself
    app = Flask(__name__)
    config = config or os.environ.get("FLASK_CONFIG", "local")
    config = pathlib.Path(__file__).absolute().parent.joinpath("config", f"{config}.py")
    app.config.from_pyfile(config)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # db
    db.init_app(app)
    migrate.init_app(app, directory=str("app/db/migrations"))

    # auth
    login_manager = LoginManager(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of my user table, use it in the query for the user
        return User.query.get(int(user_id))

    # points with render templates
    app.register_blueprint(simple_api.bp)

    # api for async
    rest_api.init_app(app)

    return app
