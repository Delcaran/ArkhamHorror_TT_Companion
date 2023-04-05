import os
import json
from enum import Enum
from typing import TypedDict

import location
from common import Check, SkillCheck
from ancient import Ancient
from investigator import Investigator
from monster import Monster


class MonsterLocation(Enum):
    NORMAL = 1
    outskirts = 2
    TERROR = 3


class JsonBoard(TypedDict):
    arkham: dict[str, location.JsonBoardLocation]
    outer_worlds: list[str]


class Board:
    GATE_TOKENS: int = 49

    def __init__(self) -> None:
        self._terror_level: int = 0
        self._ancient: Ancient | None = None
        self._sky: list[Monster] = []
        self._outskirts: list[Monster] = []
        self._arkham_locations: list[location.ArkhamLocation] = []
        self._outer_worlds: list[location.OuterWorldLocation] = []

        with open(os.path.join("data", "board.json"), "r") as j:
            data: JsonBoard = json.load(j)
            for street_name, info in data["arkham"].items():
                street = location.ArkhamLocation(street_name)
                for place_name in info["places"]:
                    place = location.ArkhamLocation(place_name)
                    # TODO: add links to place->street
                    # TODO: add links to street->places
                    self._arkham_locations.append(place)
                # TODO: add link street->street
                self._arkham_locations.append(street)
            for world_name in data["outer_worlds"]:
                self._outer_worlds.append(
                    location.OuterWorldLocation(world_name))

    def num_investigators(self) -> int:
        n = 0
        for a in self._arkham_locations + self._outer_worlds:
            n += a.num_investigators()
        return n

    def open_gates(self) -> int:
        open = 0
        for a in self._arkham_locations:
            open += 1 if a.open_gate() else 0
        return open

    def gate_thropies(self) -> int:
        thropies = 0
        for a in self._arkham_locations + self._outer_worlds:
            for i in a.investigators():
                thropies += i.gate_thropies()
        return thropies

    def elder_signs(self) -> int:
        signs = 0
        for a in self._arkham_locations:
            signs += 1 if a.elder_sign() else 0
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
    #        return MonsterLocation.NORMAL
    #    else:
    #        active_monsters = len(self._monsters["arkham"]) + len(self._monsters["sky"])
    #        if active_monsters < self.num_investigators + 3:
    #            return MonsterLocation.NORMAL
    #        elif active_monsters == self.num_investigators + 3:
    #            return MonsterLocation.outskirts
    #        elif len(self._monsters["outskirts"]) < 8 - self.num_investigators:
    #            return MonsterLocation.outskirts
    #        else:
    #            return MonsterLocation.TERROR

    def stores(self) -> dict[str, bool]:
        return {
            "General Store": self._terror_level < 3,
            "Curiositie Shoppe": self._terror_level < 6,
            "Ye Old Magick Shoppe": self._terror_level < 9
        }

    def encounter(self, investigator: Investigator, monster: Monster) -> dict[SkillCheck, Check]:
        data: dict[SkillCheck, Check] = {
            SkillCheck.EVADE: Check(investigator.evade+monster.awareness, monster.evade_check),
            SkillCheck.HORROR: Check(investigator.horror+monster.horror_rating, monster.horror_check),
        }
