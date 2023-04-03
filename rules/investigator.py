class Skill:
    def __init__(self) -> None:
        self._base : int = 0
        self._bonus : int = 0

    def get(self) -> int:
        return self._base + self._bonus

    def set(self, value:int) -> None:
        self._base = value

    def add_bonus(self, value:int) -> None:
        self._bonus += value

    def remove_bonus(self, value:int) -> None:
        self._bonus -= value


class Investigator:
    def __init__(self) -> None:
        self._health : Skill | None = None
        self._sanity : Skill | None = None
        self._focus : Skill | None = None

        self._speed : Skill | None = None
        self._sneak : Skill | None = None
        self._fight : Skill | None = None
        self._will : Skill | None = None
        self._lore : Skill | None = None
        self._luck : Skill | None = None
        self._evade_bonus : int = 0
        self._horror_bonus : int = 0
        self._combat_bonus : int = 0
        self._spell_bonus : int = 0

        self._gate_trophies : int = 0
        self._monster_trophies : int = 0
        self._loans : int = 0
        self._clues : int = 0
        self._elder_sign_played : int = 0
        self._elder_sign_owned : int = 0

    @property
    def evade(self) -> int:
        return self._sneak.get() + self._evade_bonus

    @property
    def horror(self) -> int:
        return self._will.get() + self._horror_bonus

    @property
    def combat(self) -> int:
        return self._fight.get() + self._combat_bonus

    @property
    def spell(self) -> int:
        return self._lore.get() + self._spell_bonus

    @property
    def gate_thropies(self)->int:
        return self._gate_trophies

    @property
    def alive(self)->bool:
        return (self._health > 0) and (self._sanity > 0)

    @property
    def score(self)->int:
        return self._loans*-1 + self._elder_sign_played*-1 + self.gate_thropies + self._monster_trophies/3 + 1 if self.alive() else 0