import copy
from typing import TypedDict
from enum import Enum

from . import investigator, monster


class LinksColor(Enum):
    NONE = "none"
    BLACK = "black"
    WHITE = "white"
    BOTH = "both"

class JsonBoardLocation(TypedDict):
    places: list[str]
    links: dict[str, str]


class ArkhamLocation():
    def __init__(self, name: str) -> None:
        self._name : str = name
        self._investigators : list[investigator.Investigator] = []
        self._monsters : list[monster.Monster] = []
        self._links : dict[LinksColor, list[ArkhamLocation]] = {}
        self._gate : str = ""
        self._elder_sign : bool = False
        self._clues : int = 0
        self._street : bool = False

    @property
    def street(self) -> bool:
        return self._street

    @property
    def name(self) -> str:
        return self._name

    def opened_gate(self) -> bool:
        return len(self._gate) > 0

    def num_investigators(self) -> int:
        return len(self._investigators)

    @property
    def investigators(self) -> list[investigator.Investigator]:
        return self._investigators

    @property
    def elder_sign(self) -> bool:
        return self._elder_sign

    def add_link(self, color:LinksColor, loc:'ArkhamLocation') -> None:
        if color not in self._links.keys():
            self._links[color] = []
        self._links[color].append(loc)
        self._street = len(self._links.keys()) > 1 or len(self._links[color]) > 1

class OuterWorldLocation():
    def __init__(self, name: str) -> None:
        self._name : str = name
        self._zone_one : list[investigator.Investigator] = []
        self._zone_two : list[investigator.Investigator] = []

    @property
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