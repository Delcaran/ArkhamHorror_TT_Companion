from dataclasses import dataclass
from enum import Enum


@dataclass
class Check:
    dice: int = 0
    success: int = 0


class SkillCheck(Enum):
    EVADE = "EVADE"
    HORROR = "HORROR"
    COMBAT = "COMBAT"
    SPELL = "SPELL"


class LinksColor(Enum):
    NONE = "none"
    BLACK = "black"
    WHITE = "white"
    BOTH = "both"


class Signs(Enum):
    MOON = "moon"
    STAR = "star"


class Movement(Enum):
    NORMAL = 1
    STATIONARY = 2
    FAST = 3
    UNIQUE = 4
    FLYING = 5
