from pydantic import BaseModel, PrivateAttr
from typing import TypedDict
import random
import datetime

random.seed(datetime.datetime.now().microsecond)


class Statistic(BaseModel):
    _current: int = PrivateAttr()
    _bonus: int = PrivateAttr()
    _default: int = PrivateAttr()
    _max: int = PrivateAttr()

    def init(self, max: int = 0) -> None:
        self._current: int = 0
        self._bonus: int = 0
        self._default: int = max
        self._max: int = max
        # TODO: remove when real data
        if max == 0:
            self._default = random.randrange(3, 6)
            self._max = self._default

    @property
    def current(self) -> int:
        return self._current

    @property
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
            self._current = min(tmp, self.max)
        return self._current

    # for focus only
    def reset(self) -> int:
        self._current = self._default
        return self._current


class Skill(BaseModel):
    _current: int = PrivateAttr()
    _bonus: int = PrivateAttr()
    _min: int = PrivateAttr()
    _max: int = PrivateAttr()

    def get(self) -> int:
        return self._current + self._bonus

    @property
    def max(self) -> int:
        return self._max

    @property
    def min(self) -> int:
        return self._min

    def init(self, value: int, min: int = 0, max: int = 0) -> int:
        self._min: int = min
        self._max: int = max
        # TODO: remove when real data
        if min == 0 and max == 0:
            self._min = random.randrange(1, 3)
            self._max = self._min + 3
        if self._min <= value and value <= self._max:
            self._current = value
        else:
            self._current = self._min + ((self._max - self._min) // 2) + 1
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


class Investigator(BaseModel):
    _name: str = PrivateAttr()
    _occupation: str = PrivateAttr()
    _home: str = PrivateAttr()
    _stamina: Statistic = PrivateAttr()
    _sanity: Statistic = PrivateAttr()
    _focus: Statistic = PrivateAttr()
    _temp_focus: int = PrivateAttr()

    _speed: Skill = PrivateAttr()
    _sneak: Skill = PrivateAttr()
    _fight: Skill = PrivateAttr()
    _will: Skill = PrivateAttr()
    _lore: Skill = PrivateAttr()
    _luck: Skill = PrivateAttr()
    _evade_bonus: int = PrivateAttr()
    _horror_bonus: int = PrivateAttr()
    _combat_bonus: int = PrivateAttr()
    _spell_bonus: int = PrivateAttr()

    _gate_trophies: int = PrivateAttr()
    _monster_trophies: int = PrivateAttr()
    _loans: int = PrivateAttr()
    _clues: int = PrivateAttr()
    _elder_sign_played: int = PrivateAttr()
    _elder_sign_owned: int = PrivateAttr()

    def init(self, name: str, data: JsonInvestigator) -> None:
        self._name = name
        self._occupation = data["occupation"]
        self._home = data["home"]
        self._stamina = Statistic(_max=data["stamina"])
        self._sanity = Statistic(_max=data["sanity"])
        self._focus = Statistic(_max=data["focus"])
        self._speed = Skill(
            _min=data["speed"]["min"], _max=data["speed"]["max"])
        self._sneak = Skill(
            _min=data["sneak"]["min"], _max=data["sneak"]["max"])
        self._fight = Skill(
            _min=data["fight"]["min"], _max=data["fight"]["max"])
        self._will = Skill(_min=data["will"]["min"], _max=data["will"]["max"])
        self._lore = Skill(_min=data["lore"]["min"], _max=data["lore"]["max"])
        self._luck = Skill(_min=data["luck"]["min"], _max=data["luck"]["max"])

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
    def gate_thropies(self) -> int:
        return self._gate_trophies

    @property
    def alive(self) -> bool:
        return (self._stamina.current > 0) and (self._sanity.current > 0)

    @property
    def score(self) -> int:
        return self._loans*-1 + self._elder_sign_played*-1 + self.gate_thropies + self._monster_trophies//3 + 1 if self.alive else 0

    def sanity_damage(self, value: int) -> int:
        return self._sanity.damage(value)

    def sanity_heal(self, value: int | None) -> int:
        return self._sanity.heal(value)

    def stamina_damage(self, value: int) -> int:
        return self._stamina.damage(value)

    def stamina_heal(self, value: int | None) -> int:
        return self._stamina.heal(value)
