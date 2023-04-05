from dataclasses import dataclass
from enum import Enum

@dataclass
class Check:
    dice : int = 0
    success : int = 0

class SkillCheck(Enum):
    EVADE = "EVADE"
    HORROR = "HORROR"
    COMBAT = "COMBAT"
    SPELL = "SPELL"
