from enum import Enum

class Movement(Enum):
    NORMAL = 1
    STATIONARY = 2
    FAST = 3
    UNIQUE = 4
    FLYING = 5

class Sign(Enum):
    MOON = 1
    SQUARE = 2
    CIRCLE = 3

class Monster:
    def __init__(self) -> None:
        self._name : str = ""
        self._movement : Movement | None = None
        self._sign : Sign | None = None
        self._awareness : int = 0
        self._evade_check : int = 0
        self._horror_rating : int = 0
        self._horror_check : int = 0
        self._sanity_damage : int = 0
        self._combat_rating : int = 0
        self._toughness : int = 0
        self._combat_damage : int = 0