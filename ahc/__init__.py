from flask import Flask
from typing import Any


def create_app(test_config: dict[str, Any] | None = None):
    from os import path

    app = Flask(__name__)
    app.config.from_mapping(
        DATA_PATH=path.join(path.dirname(path.abspath(__file__)), 'data'),
        SECRET_KEY='dev',
        #DATABASE=path.join(app.instance_path, 'ahc.sqlite'),
        DATABASE=path.join(path.dirname(path.abspath(__file__)), 'ahc.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import board
    app.register_blueprint(board.bp)
    app.add_url_rule("/", endpoint="index")

    return app
