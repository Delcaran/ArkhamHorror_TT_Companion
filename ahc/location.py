import copy
from typing import TypedDict

from . import investigator, monster, common


class JsonBoardLocation(TypedDict):
    places: list[str]
    links: dict[str, str]


class ArkhamLocation():
    def __init__(self, name: str, street: bool = False) -> None:
        self._name: str = name
        self._investigators: list[investigator.Investigator] = []
        self._monsters: list[monster.Monster] = []
        self._gate: str = ""
        self._elder_sign: bool = False
        self._clues: int = 0
        self._street: bool = street

    @property
    def street(self) -> bool:
        return self._street

    @property
    def name(self) -> str:
        return self._name

    @property
    def investigators(self) -> list[investigator.Investigator]:
        return self._investigators

    @property
    def elder_sign(self) -> bool:
        return self._elder_sign

    def opened_gate(self) -> bool:
        return len(self._gate) > 0

    def num_investigators(self) -> int:
        return len(self._investigators)

    def add_monster(self, monster: monster.Monster) -> int:
        self._monsters.append(monster)
        return len(self._monsters) - 1

    def remove_monster(self, monster_id: int) -> monster.Monster | None:
        try:
            return self._monsters.pop(monster_id)
        except IndexError:
            return None

    def add_investigator(self, investigator: investigator.Investigator) -> int:
        self._investigators.append(investigator)
        return len(self._investigators) - 1

    def remove_investigator(self, investigator_id: int) -> investigator.Investigator | None:
        try:
            return self._investigators.pop(investigator_id)
        except IndexError:
            return None


class OuterWorldLocation():
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._zone_one: list[investigator.Investigator] = []
        self._zone_two: list[investigator.Investigator] = []

    @property
    def name(self) -> str:
        return self._name

    def next(self) -> list[investigator.Investigator]:
        outgoing: list[investigator.Investigator] = copy.copy(self._zone_two)
        self._zone_two = copy.copy(self._zone_one)
        self._zone_one = list()
        return outgoing

    def num_investigators(self) -> int:
        return len(self._zone_one) + len(self._zone_two)

    def investigators(self) -> list[investigator.Investigator]:
        return self._zone_one + self._zone_two
