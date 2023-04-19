from flask import Blueprint, redirect, url_for
from ahc.models import Player, Investigator

bp = Blueprint("player", __name__, url_prefix='/player')


@bp.route("/<skill>/add/<player_id>", methods=["GET"])
def add_skill(skill: str, player_id: int):
    player: Player = Player.get_by_id(player_id)
    if skill == "sneak":
        next = player.sneak + 1
        if next <= player.investigator.sneak_max:
            query = player.update({
                Player.sneak: player.sneak + 1,
                Player.speed: player.speed - 1
            })
    elif skill == "speed":
        next = player.speed + 1
        if next <= player.investigator.speed_max:
            query = player.update({
                Player.speed: player.speed + 1,
                Player.sneak: player.sneak - 1
            })
    elif skill == "fight":
        next = player.fight + 1
        if next <= player.investigator.fight_max:
            query = player.update({
                Player.fight: player.fight + 1,
                Player.will: player.will - 1
            })
    elif skill == "will":
        next = player.will + 1
        if next <= player.investigator.will_max:
            query = player.update({
                Player.will: player.will + 1,
                Player.fight: player.fight - 1
            })
    elif skill == "lore":
        next = player.lore + 1
        if next <= player.investigator.lore_max:
            query = player.update({
                Player.lore: player.lore + 1,
                Player.luck: player.luck - 1
            })
    elif skill == "luck":
        next = player.luck + 1
        if next <= player.investigator.luck_max:
            query = player.update({
                Player.luck: player.luck + 1,
                Player.lore: player.lore - 1
            })
    query.execute()

    return redirect(url_for("board.index"))
