from flask import Blueprint, render_template

bp = Blueprint("board", __name__)


@bp.route("/", methods=["GET"])
def index():
    # gameboard = Board()
    return render_template(
        "board/main.html",
        # arkham_locations=gameboard.arkham_locations,
        # outer_worlds=gameboard.outer_worlds
    )
