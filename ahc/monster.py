from pydantic import BaseModel, PrivateAttr

from . import common


class Monster(BaseModel):
    _name: str = PrivateAttr()
    _movement: common.Movement = PrivateAttr()
    _sign: common.Signs = PrivateAttr()
    _awareness: int = PrivateAttr()
    _evade_check: int = PrivateAttr()
    _horror_rating: int = PrivateAttr()
    _horror_check: int = PrivateAttr()
    _sanity_damage: int = PrivateAttr()
    _combat_rating: int = PrivateAttr()
    _toughness: int = PrivateAttr()
    _combat_damage: int = PrivateAttr()

    @property
    def name(self) -> str:
        return self._name

    @property
    def movement(self) -> common.Movement:
        return self._movement

    @property
    def sign(self) -> common.Signs:
        return self._sign

    @property
    def awareness(self) -> int:
        return self._awareness

    @property
    def evade_check(self) -> int:
        return self._evade_check

    @property
    def horror_rating(self) -> int:
        return self._horror_rating

    @property
    def horror_check(self) -> int:
        return self._horror_check

    @property
    def sanity_damage(self) -> int:
        return self._sanity_damage

    @property
    def combat_rating(self) -> int:
        return self._combat_rating

    @property
    def toughness(self) -> int:
        return self._toughness

    @property
    def combat_damage(self) -> int:
        return self._combat_damage
