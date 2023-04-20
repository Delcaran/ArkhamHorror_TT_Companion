from flask import Blueprint, render_template, g
from ahc.models import Location, Monster, Player
from typing import Union

bp = Blueprint("board", __name__)


@bp.route("/", methods=["GET"])
def index():
    player : Player = g.player
    locations : list[Location] = Location.select()
    monsters : list[Monster] = Monster.select().where((Monster.location.is_null(False)) & (Monster.sky==False) & (Monster.outskirts==False))
    vs : dict[int, dict[str, Union[int, str]]] = {}
    for monster in monsters:
        # TODO calcolare il totale del giocatore con bonus e malus
        # TODO inserire anche l'ambiente
        evade = player.sneak + monster.awareness
        terror = player.will + monster.horror_rating
        combat = player.fight + monster.combat_rating
        evade_class = ""
        terror_class = ""
        combat_class = ""
        if monster.sanity_damage > player.sanity:
            if terror < monster.horror_check:
                terror_class = "fatal"
            else:
                terror_class = "deadly"
        if monster.combat_damage > player.stamina:
            if combat < monster.toughness:
                combat_class = "fatal"
            else:
                combat_class = "deadly"
        vs[monster.id] = {
            "evade": evade,
            "terror": terror,
            "combat": combat,
            "evade_class": evade_class,
            "terror_class": terror_class,
            "combat_class": combat_class
        }
    return render_template(
        "board/main.html",
        locations = locations,
        monsters = monsters,
        vs = vs,
        player = player
    )
