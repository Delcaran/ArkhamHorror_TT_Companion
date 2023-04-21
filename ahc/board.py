from flask import Blueprint, render_template, g, redirect, url_for
from ahc.models import Location, Monster, Player
from typing import Union

bp = Blueprint("board", __name__)


def get_vs_class(player_dice: int, successes: int, health: int, damage: int) -> str:
    if player_dice < successes:
        if health > 0:
            if damage > health:
                return "fatal"
            else:
                return "deadly"
    return ""


@bp.route("/", methods=["GET"])
def index():
    player: Player = g.player
    # locations : list[Location] = Location.select()
    monsters: list[Monster] = Monster.select().order_by(Monster.name)
    vs: dict[int, dict[str, Union[int, str]]] = {}
    for monster in monsters:
        # TODO calcolare il totale del giocatore con bonus e malus
        # TODO inserire anche l'ambiente
        evade = player.sneak if player else 0 + monster.awareness
        terror = player.will if player else 0 + monster.horror_rating
        combat = player.fight if player else 0 + monster.combat_rating
        evade_class = get_vs_class(
            evade, 
            monster.evade_check, 
            player.stamina if player else -1, 
            monster.combat_damage)
        terror_class = get_vs_class(
            terror, 
            monster.horror_check, 
            player.sanity if player else -1, 
            monster.sanity_damage)
        combat_class = get_vs_class(
            combat, 
            monster.toughness, 
            player.stamina if player else -1, 
            monster.combat_damage)
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
        # locations = locations,
        monsters=monsters,
        vs=vs,
        player=player
    )
