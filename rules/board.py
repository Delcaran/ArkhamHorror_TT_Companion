from typing import List

import ancient
import investigator

class Board:
    AVAILABLE_GATE_TOKENS : int = 49

    def __init__(self) -> None:
        self._open_gates: int = 0
        self._elder_signs: int = 0
        self._ancient : ancient.Ancient | None = None
        self._investigators : List[investigator.Investigator] = []

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
