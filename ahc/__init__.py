from flask import Flask
from typing import Any
from peewee import SqliteDatabase
from werkzeug.serving import is_running_from_reloader

database = SqliteDatabase(':memory:')


def create_app(test_config: dict[str, Any] | None = None) -> Flask:
    global database
    #from os import path
    #app_root = path.dirname(path.abspath(__file__))

    app = Flask(__name__)
    database = SqliteDatabase("ahc.sqlite", pragmas=[('journal_mode', 'wal')])
    app.config.from_mapping(SECRET_KEY='dev')

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
    app.add_url_rule("/", endpoint="index")

    return app
