import copy
from typing import TypedDict

from investigator import Investigator
from monster import Monster


class JsonBoardLocation(TypedDict):
    places: list[str]
    links: dict[str, str]


class ArkhamLocation():
    def __init__(self, name: str) -> None:
        self._name : str = name
        self._investigators : list[Investigator] = []
        self._monsters : list[Monster] = []
        self._links : list[ArkhamLocation] = []
        self._gate : str = ""
        self._elder_sign : bool = False
        self._clues : int = 0

    def open_gate(self) -> bool:
        return len(self._gate) > 0

    def num_investigators(self) -> int:
        return len(self._investigators)

    def investigators(self) -> list[Investigator]:
        return self._investigators

    def elder_sign(self) -> bool:
        return self._elder_sign

class OuterWorldLocation():
    def __init__(self, name: str) -> None:
        self._name : str = name
        self._zone_one : list[Investigator] = []
        self._zone_two : list[Investigator] = []

    def next(self) -> list[Investigator]:
        outgoing :list[Investigator] = copy.copy(self._zone_two)
        self._zone_two = copy.copy(self._zone_one)
        self._zone_one = list()
        return outgoing

    def num_investigators(self) -> int:
        return len(self._zone_one) + len(self._zone_two)

    def investigators(self) -> list[Investigator]:
        return self._zone_one + self._zone_two