from flask import Flask
from typing import Any, Optional
from peewee import SqliteDatabase
from werkzeug.serving import is_running_from_reloader

database = SqliteDatabase(':memory:', pragmas={"foreign_keys": 1})


def create_app(test_config: Optional[dict[str, Any]] = None) -> Flask:
    global database
    # from os import path
    # app_root = path.dirname(path.abspath(__file__))

    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev')

    database = SqliteDatabase("ahc.sqlite", pragmas={"foreign_keys": 1})

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    if not is_running_from_reloader():
        from ahc import models
        models.init_db(database)

    from ahc import auth
    app.register_blueprint(auth.bp)

    from ahc import board
    app.register_blueprint(board.bp)

    from ahc import player
    app.register_blueprint(player.bp)

    return app
