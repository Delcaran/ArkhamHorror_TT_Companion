from . import common


class Monster:
    def __init__(self) -> None:
        self._name : str = ""
        self._movement : common.Movement | None = None
        self._sign : common.Signs | None = None
        self._awareness : int = 0
        self._evade_check : int = 0
        self._horror_rating : int = 0
        self._horror_check : int = 0
        self._sanity_damage : int = 0
        self._combat_rating : int = 0
        self._toughness : int = 0
        self._combat_damage : int = 0

    @property
    def name(self)->str:
        return self._name

    @property
    def movement(self)->common.Movement:
        return self._movement

    @property
    def sign(self)->common.Signs:
        return self._sign

    @property
    def awareness(self)->int:
        return self._awareness

    @property
    def evade_check(self)->int:
        return self._evade_check

    @property
    def horror_rating(self)->int:
        return self._horror_rating

    @property
    def horror_check(self)->int:
        return self._horror_check

    @property
    def sanity_damage(self)->int:
        return self._sanity_damage

    @property
    def combat_rating(self)->int:
        return self._combat_rating

    @property
    def toughness(self)->int:
        return self._toughness

    @property
    def combat_damage(self)->int:
        return self._combat_damage
