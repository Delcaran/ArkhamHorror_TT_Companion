from flask import Blueprint, render_template, g
from ahc.models import Location, Monster, Player

bp = Blueprint("board", __name__)


@bp.route("/", methods=["GET"])
def index():
    player : Player = g.player
    locations : list[Location] = Location.select()
    monsters : list[Monster] = Monster.select().where((Monster.location.is_null(False)) & (Monster.sky==False) & (Monster.outskirts==False))
    vs : dict[int, dict[str, int]] = {}
    for monster in monsters:
        # TODO calcolare il totale del giocatore con bonus e malus
        # TODO inserire anche l'ambiente
        vs[monster.id] = {
            "evade": player.sneak + monster.awareness,
            "terror": player.will + monster.horror_rating,
            "combat": player.fight + monster.combat_rating 
        }
    return render_template(
        "board/main.html",
        locations = locations,
        monsters = monsters,
        vs = vs
    )
