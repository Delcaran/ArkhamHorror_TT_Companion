from typing import List, Dict
from enum import Enum

import ancient
import investigator
import monster

class MonsterLocation(Enum):
    NORMAL = 1
    SUBURBS = 2
    TERROR = 3

class Board:
    AVAILABLE_GATE_TOKENS : int = 49

    def __init__(self) -> None:
        self._open_gates: int = 0
        self._elder_signs: int = 0
        self._terror_level : int = 0
        self._ancient : ancient.Ancient | None = None
        self._investigators : List[investigator.Investigator] = []
        self._monsters : Dict[str, List[monster.Monster]] = {"arkham":[], "sky":[], "suburbs":[]}

    @property
    def num_investigators(self) -> int:
        return len(self._investigators)

    @property
    def num_investigators(self) -> int:
        return len(self._investigators)

    @property
    def num_portals(self) -> int:
        return self._open_gates

    def victory(self) -> bool:
        if self._open_gates == 0:
            total_thropies = 0
            for i in self._investigators:
                total_thropies += i.gate_thropies
                if total_thropies >= self.num_investigators():
                    return True
        elif self._elder_signs >= 6:
            return True
        else:
            return False

    def ancient_awakes(self) -> bool:
        if self._ancient.doom_track_full():
            return True
        else:
            if self.num_investigators() == 1 or self.num_investigators() == 2:
                return self._open_gates == 8
            elif self.num_investigators() == 3 or self.num_investigators() == 4:
                return self._open_gates == 7
            elif self.num_investigators() == 5 or self.num_investigators() == 6:
                return self._open_gates == 6
            elif self.num_investigators() == 7 or self.num_investigators() == 8:
                return self._open_gates == 5
            else:
                return Board.AVAILABLE_GATE_TOKENS == 0

    def next_monster_location(self) -> MonsterLocation:
        if self._terror_level < 10:
            return MonsterLocation.NORMAL
        else:
            active_monsters = len(self._monsters["arkham"]) + len(self._monsters["sky"])
            if active_monsters < self.num_investigators + 3:
                return MonsterLocation.NORMAL
            elif active_monsters == self.num_investigators + 3:
                return MonsterLocation.SUBURBS
            elif len(self._monsters["suburbs"]) < 8 - self.num_investigators:
                return MonsterLocation.SUBURBS
            else:
                return MonsterLocation.TERROR

    def stores(self) -> Dict[str, bool]:
        return {
            "General Store": self._terror_level < 3,
            "Curiositie Shoppe": self._terror_level < 6,
            "Ye Old Magick Shoppe": self._terror_level < 9
        }
