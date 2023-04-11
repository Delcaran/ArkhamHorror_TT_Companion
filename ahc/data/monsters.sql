DROP TABLE IF EXISTS monster_sign;
CREATE TABLE monster_sign (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);
INSERT INTO monster_sign (name) VALUES
("moon"),
("circle")
;

DROP TABLE IF EXISTS monster;
CREATE TABLE monster (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL,
	sign INTEGER NOT NULL,
	awareness INTEGER NOT NULL,
	evade_check INTEGER NOT NULL,
	horror_rating INTEGER NOT NULL,
	horror_check INTEGER NOT NULL,
	sanity_damage INTEGER NOT NULL,
	combat_rating INTEGER NOT NULL,
	toughness INTEGER NOT NULL,
	combat_damage INTEGER NOT NULL
);
INSERT INTO monster (name, sign, awareness, evade_check, horror_rating, horror_check, sanity_damage, combat_rating, toughness, combat_damage) VALUES
("cicciolo", (SELECT id FROM monster_sign WHERE name="moon"), 1, 2, 1, 2, 1, 2, 1, 2),
("bombolo", (SELECT id FROM monster_sign WHERE name="circle"), 1, 2, 1, 2, 1, 2, 1, 2)
;