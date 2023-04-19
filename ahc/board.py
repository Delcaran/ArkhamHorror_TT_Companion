from flask import Blueprint, render_template
from ahc.models import Location

bp = Blueprint("board", __name__)


@bp.route("/", methods=["GET"])
def index():
    locations = Location.select()
    return render_template(
        "board/main.html",
        locations = locations
    )
