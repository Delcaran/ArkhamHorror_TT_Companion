from typing import TypedDict


class Statistic:
    def __init__(self, max: int = 0) -> None:
        self._current: int = 0
        self._bonus: int = 0
        self._default: int = max
        self._max: int = max

    def max(self) -> int:
        return self._max + self._bonus

    def damage(self, value: int = 1) -> int:
        tmp = self._current - value
        self._current = max(0, tmp)
        return self._current

    def heal(self, value: int | None) -> int:
        if not value:
            self._current = 1
        else:
            tmp = self._current + value
            self._current = min(tmp, self.max())
        return self._current

    # for focus only
    def reset(self) -> int:
        self._current = self._default
        return self._current


class Skill:
    def __init__(self, min: int = 0, max: int = 0) -> None:
        self._current: int = 0
        self._bonus: int = 0
        self._min: int = min
        self._max: int = max

    def get(self) -> int:
        return self._current + self._bonus

    def max(self) -> int:
        return self._max

    def min(self) -> int:
        return self._min

    def init(self, value: int) -> int:
        if self._min <= value and value <= self._max:
            self._current = value
        else:
            self._current = self._min + round((self._max - self._min)/2, 0)
        return self.get()

    def increase(self, value: int = 1) -> int:
        tmp = self._current + value
        self._current = min(tmp, self._max)
        return self.get()

    def decrease(self, value: int = 1) -> int:
        tmp = self._current - value
        self._current = max(tmp, self._min)
        return self.get()

    def add_bonus(self, value: int) -> None:
        self._bonus += value

    def remove_bonus(self, value: int) -> None:
        self._bonus -= value


class JsonSkill(TypedDict):
    min: int
    max: int


class JsonInvestigator(TypedDict):
    occupation: str
    home: str
    stamina: int
    sanity: int
    focus: int
    speed: JsonSkill
    sneak: JsonSkill
    fight: JsonSkill
    will: JsonSkill
    lore: JsonSkill
    luck: JsonSkill


class Investigator:
    def __init__(self) -> None:
        self._name: str = ""
        self._occupation: str = ""
        self._home: str = ""
        self._stamina: Statistic | None = None
        self._sanity: Statistic | None = None
        self._focus: Statistic | None = None
        self._temp_focus: int = 0

        self._speed: Skill | None = None
        self._sneak: Skill | None = None
        self._fight: Skill | None = None
        self._will: Skill | None = None
        self._lore: Skill | None = None
        self._luck: Skill | None = None
        self._evade_bonus: int = 0
        self._horror_bonus: int = 0
        self._combat_bonus: int = 0
        self._spell_bonus: int = 0

        self._gate_trophies: int = 0
        self._monster_trophies: int = 0
        self._loans: int = 0
        self._clues: int = 0
        self._elder_sign_played: int = 0
        self._elder_sign_owned: int = 0

    def load(self, name: str, data: JsonInvestigator) -> None:
        self._name = name
        self._occupation = data["occupation"]
        self._home = data["home"]
        self._stamina = Statistic(max=data["stamina"])
        self._sanity = Statistic(max=data["sanity"])
        self._focus = Statistic(max=data["focus"])
        self._speed = Skill(min=data["speed"]["min"], max=data["speed"]["max"])
        self._sneak = Skill(min=data["sneak"]["min"], max=data["sneak"]["max"])
        self._fight = Skill(min=data["fight"]["min"], max=data["fight"]["max"])
        self._will = Skill(min=data["will"]["min"], max=data["will"]["max"])
        self._lore = Skill(min=data["lore"]["min"], max=data["lore"]["max"])
        self._luck = Skill(min=data["luck"]["min"], max=data["luck"]["max"])

    def evade(self) -> int:
        return self._sneak.get() + self._evade_bonus

    def horror(self) -> int:
        return self._will.get() + self._horror_bonus

    def combat(self) -> int:
        return self._fight.get() + self._combat_bonus

    def spell(self) -> int:
        return self._lore.get() + self._spell_bonus

    def gate_thropies(self) -> int:
        return self._gate_trophies

    def alive(self) -> bool:
        return (self._stamina > 0) and (self._sanity > 0)

    def score(self) -> int:
        return self._loans*-1 + self._elder_sign_played*-1 + self.gate_thropies + self._monster_trophies/3 + 1 if self.alive() else 0

    def sanity_damage(self, value: int) -> int:
        return self._sanity.damage(value)

    def sanity_heal(self, value: int | None) -> int:
        return self._sanity.heal(value)

    def stamina_damage(self, value: int) -> int:
        return self._stamina.damage(value)

    def stamina_heal(self, value: int | None) -> int:
        return self._stamina.heal(value)
