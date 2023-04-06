import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        DATA_PATH=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import board
    app.register_blueprint(board.bp)
    app.add_url_rule("/", endpoint="index")

    return app
