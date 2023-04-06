import copy
from typing import TypedDict

from . import investigator, monster


class JsonBoardLocation(TypedDict):
    places: list[str]
    links: dict[str, str]


class ArkhamLocation():
    def __init__(self, name: str) -> None:
        self._name : str = name
        self._investigators : list[investigator.Investigator] = []
        self._monsters : list[monster.Monster] = []
        self._links : list[ArkhamLocation] = []
        self._gate : str = ""
        self._elder_sign : bool = False
        self._clues : int = 0

    def street(self) -> bool:
        return len(self._links)>1

    def name(self) -> str:
        return self._name

    def open_gate(self) -> bool:
        return len(self._gate) > 0

    def num_investigators(self) -> int:
        return len(self._investigators)

    def investigators(self) -> list[investigator.Investigator]:
        return self._investigators

    def elder_sign(self) -> bool:
        return self._elder_sign

    def add_link(self, loc:'ArkhamLocation') -> None:
        self._links.append(loc)

class OuterWorldLocation():
    def __init__(self, name: str) -> None:
        self._name : str = name
        self._zone_one : list[investigator.Investigator] = []
        self._zone_two : list[investigator.Investigator] = []

    def name(self) -> str:
        return self._name

    def next(self) -> list[investigator.Investigator]:
        outgoing :list[investigator.Investigator] = copy.copy(self._zone_two)
        self._zone_two = copy.copy(self._zone_one)
        self._zone_one = list()
        return outgoing

    def num_investigators(self) -> int:
        return len(self._zone_one) + len(self._zone_two)

    def investigators(self) -> list[investigator.Investigator]:
        return self._zone_one + self._zone_two