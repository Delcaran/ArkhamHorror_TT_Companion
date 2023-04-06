import os
import json
from enum import Enum
from pydantic import BaseModel, PrivateAttr
from typing import TypedDict
from flask import Blueprint, render_template, current_app

from . import location, ancient, investigator, monster

bp = Blueprint("board", __name__)


class MonsterLocation(Enum):
    NORMAL = 1
    OUTSKIRTS = 2
    TERROR = 3


class JsonBoard(TypedDict):
    arkham: dict[str, location.JsonBoardLocation]
    outer_worlds: list[str]


class Board(BaseModel):
    GATE_TOKENS: int = 49
    _terror_level: int = PrivateAttr()
    _ancient: ancient.Ancient = PrivateAttr()
    _players: dict[str, investigator.Investigator] = PrivateAttr()
    _sky: list[monster.Monster] = PrivateAttr()
    _outskirts: list[monster.Monster] = PrivateAttr()
    _arkham_locations: list[location.ArkhamLocation] = PrivateAttr()
    _outer_worlds: list[location.OuterWorldLocation] = PrivateAttr()

    def init(self) -> None:
        with open(os.path.join(current_app.config["DATA_PATH"], "board.json"), "r") as j:
            data: JsonBoard = json.load(j)
            for street_name, info in data["arkham"].items():
                street = location.ArkhamLocation(
                    _name=street_name, _street=True)
                for place_name in info["places"]:
                    place = location.ArkhamLocation(_name=place_name)
                    # place.add_link(common.LinksColor.BOTH, street)
                    # street.add_link(common.LinksColor.NONE, place)
                    self._arkham_locations.append(place)
                self._arkham_locations.append(street)
            # for loc in self._arkham_locations:
            #    if loc.street:
            #        for link_name, link_color  in info["links"].items():
            #            for other_loc in self._arkham_locations:
            #                if other_loc.name == link_name:
            #                    loc.add_link(link_color, other_loc)
            #                    break
            for world_name in data["outer_worlds"]:
                self._outer_worlds.append(
                    location.OuterWorldLocation(_name=world_name))

    def arkham_locations(self) -> list[location.ArkhamLocation]:
        return self._arkham_locations

    def outer_worlds(self) -> list[location.OuterWorldLocation]:
        return self._outer_worlds

    def num_investigators(self) -> int:
        n = 0
        for a in self._arkham_locations + self._outer_worlds:
            n += a.num_investigators()
        return n

    def open_gates(self) -> int:
        open = 0
        for a in self._arkham_locations:
            open += 1 if a.opened_gate() else 0
        return open

    def gate_thropies(self) -> int:
        thropies = 0
        for a in self._arkham_locations + self._outer_worlds:
            for i in a.investigators:
                thropies += i.gate_thropies
        return thropies

    def elder_signs(self) -> int:
        signs = 0
        for a in self._arkham_locations:
            signs += 1 if a.elder_sign else 0
        return signs

    def victory(self) -> bool:
        if self.open_gates() == 0:
            total_thropies = self.gate_thropies()
            return total_thropies >= self.num_investigators()
        elif self.elder_signs() >= 6:
            return True
        else:
            return False

    def ancient_awakes(self) -> bool:
        if self._ancient.doom_track_full():
            return True
        else:
            num_investigators = self.num_investigators()
            open_gates = self.open_gates()
            if num_investigators == 1 or num_investigators == 2:
                return open_gates == 8
            elif num_investigators == 3 or num_investigators == 4:
                return open_gates == 7
            elif num_investigators == 5 or num_investigators == 6:
                return open_gates == 6
            elif num_investigators == 7 or num_investigators == 8:
                return open_gates == 5
            else:
                return Board.GATE_TOKENS == (open_gates + self.gate_thropies())

    # def next_monster_location(self) -> MonsterLocation:
    #    if self._terror_level < 10:
    #        return MonsterNORMAL
    #    else:
    #        active_monsters = len(self._monsters["arkham"]) + len(self._monsters["sky"])
    #        if active_monsters < self.num_investigators + 3:
    #            return MonsterNORMAL
    #        elif active_monsters == self.num_investigators + 3:
    #            return Monsteroutskirts
    #        elif len(self._monsters["outskirts"]) < 8 - self.num_investigators:
    #            return Monsteroutskirts
    #        else:
    #            return MonsterTERROR

    def stores(self) -> dict[str, bool]:
        return {
            "General Store": self._terror_level < 3,
            "Curiositie Shoppe": self._terror_level < 6,
            "Ye Old Magick Shoppe": self._terror_level < 9
        }


@bp.route("/", methods=["GET"])
def index():
    gameboard = Board()
    return render_template(
        "board/main.html",
        arkham_locations=gameboard.arkham_locations(),
        outer_worlds=gameboard.outer_worlds()
    )
