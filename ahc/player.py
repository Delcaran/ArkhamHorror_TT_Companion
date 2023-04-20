from flask import Blueprint, redirect, url_for
from ahc.models import Player, Investigator

bp = Blueprint("player", __name__, url_prefix='/player')


@bp.route("<player_id>/<stat>/heal", methods=["GET"])
def heal_stat(stat: str, player_id: int):
    player: Player = Player.get_by_id(player_id)
    if stat == "stamina" and player.stamina + 1 <= player.investigator.stamina:  # TODO: verificare questo limite
        player.update({Player.stamina: player.stamina + 1}).execute()
    elif stat == "sanity" and player.sanity + 1 <= player.investigator.sanity:  # TODO: verificare questo limite
        player.update({Player.sanity: player.sanity + 1}).execute()
    else:
        pass
    return redirect(url_for("board.index"))


@bp.route("<player_id>/<stat>/damage", methods=["GET"])
def damage_stat(stat: str, player_id: int):
    player: Player = Player.get_by_id(player_id)
    if stat == "stamina" and player.stamina - 1 >= 0:
        player.update({Player.stamina: player.stamina - 1}).execute()
    elif stat == "sanity" and player.sanity - 1 >= 0:
        player.update({Player.sanity: player.sanity - 1}).execute()
    else:
        pass
    return redirect(url_for("board.index"))


@bp.route("<player_id>/<skill>/add", methods=["GET"])
def add_skill(skill: str, player_id: int):
    player: Player = Player.get_by_id(player_id)
    if skill == "sneak":
        next = player.sneak + 1
        if next <= player.investigator.sneak_max:
            player.update({
                Player.sneak: player.sneak + 1,
                Player.speed: player.speed - 1
            }).execute()
    elif skill == "speed":
        next = player.speed + 1
        if next <= player.investigator.speed_max:
            player.update({
                Player.speed: player.speed + 1,
                Player.sneak: player.sneak - 1
            }).execute()
    elif skill == "fight":
        next = player.fight + 1
        if next <= player.investigator.fight_max:
            player.update({
                Player.fight: player.fight + 1,
                Player.will: player.will - 1
            }).execute()
    elif skill == "will":
        next = player.will + 1
        if next <= player.investigator.will_max:
            player.update({
                Player.will: player.will + 1,
                Player.fight: player.fight - 1
            }).execute()
    elif skill == "lore":
        next = player.lore + 1
        if next <= player.investigator.lore_max:
            player.update({
                Player.lore: player.lore + 1,
                Player.luck: player.luck - 1
            }).execute()
    elif skill == "luck":
        next = player.luck + 1
        if next <= player.investigator.luck_max:
            player.update({
                Player.luck: player.luck + 1,
                Player.lore: player.lore - 1
            }).execute()
    else:
        pass

    return redirect(url_for("board.index"))
