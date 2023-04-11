import copy
from pydantic import BaseModel, PrivateAttr
from typing import TypedDict

from ahc import investigator, monster


class ArkhamLocation(BaseModel):
    _id : int = PrivateAttr()
    _name: str = PrivateAttr()
    _investigators: list[investigator.Investigator] = PrivateAttr()
    _monsters: list[monster.Monster] = PrivateAttr()
    _gate: str = PrivateAttr()
    _elder_sign: bool = PrivateAttr()
    _clues: int = PrivateAttr()
    _street: bool = PrivateAttr()

    def __init__(self, id:int, name:str, street:bool, **data) -> None:
        super().__init__(**data)
        self._id = id
        self._name = name
        self._street = street

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


class OuterWorldLocation(BaseModel):
    _id : int = PrivateAttr()
    _name: str = PrivateAttr()
    _zone_one: list[investigator.Investigator] = PrivateAttr()
    _zone_two: list[investigator.Investigator] = PrivateAttr()

    def __init__(self, id:int, name:str, **data) -> None:
        super().__init__(**data)
        self._id = id
        self._name = name

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

    @property
    def investigators(self) -> list[investigator.Investigator]:
        return self._zone_one + self._zone_two
