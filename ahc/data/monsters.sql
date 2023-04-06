DROP TABLE IF EXISTS monster;
CREATE TABLE monster (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL,
	sign TEXT NOT NULL,
	awareness INTEGER NOT NULL,
	evade_check INTEGER NOT NULL,
	horror_rating INTEGER NOT NULL,
	horror_check INTEGER NOT NULL,
	sanity_damage INTEGER NOT NULL,
	combat_rating INTEGER NOT NULL,
	toughness INTEGER NOT NULL,
	combat_damage INTEGER NOT NULL
);
