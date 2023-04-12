DROP TABLE IF EXISTS investigator_card;
CREATE TABLE investigator_card (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL,
	occupation TEXT NOT NULL,
	home INTEGER NOT NULL,
	stamina INTEGER NOT NULL,
	sanity INTEGER NOT NULL,
	focus INTEGER NOT NULL,
	speed_min INTEGER NOT NULL,
	speed_max INTEGER NOT NULL,
	sneak_min INTEGER NOT NULL,
	sneak_max INTEGER NOT NULL,
	fight_min INTEGER NOT NULL,
	fight_max INTEGER NOT NULL,
	will_min INTEGER NOT NULL,
	will_max INTEGER NOT NULL,
	lore_min INTEGER NOT NULL,
	lore_max INTEGER NOT NULL,
	luck_min INTEGER NOT NULL,
	luck_max INTEGER NOT NULL
);
INSERT INTO investigator_card (name, occupation, home, stamina, sanity, focus, speed_min, speed_max, sneak_min, sneak_max, fight_min, fight_max, will_min, will_max, lore_min, lore_max, luck_min, luck_max)
VALUES
("Amanda Sharpe", "student", (SELECT id FROM arkham_location WHERE name="bank of arkham"), 5, 5, 3, 0,0,0,0,0,0,0,0,0,0,0,0),
("'Ashcan' Pete", "drifter", (SELECT id FROM arkham_location WHERE name="river docks"), 6, 4, 1, 0,0,0,0,0,0,0,0,0,0,0,0),
("Bob Jenkins", "salesman", (SELECT id FROM arkham_location WHERE name="general store"), 4, 6, 1, 0,0,0,0,0,0,0,0,0,0,0,0)
;

-- DINAMIC DATA

DROP TABLE IF EXISTS investigator;
CREATE TABLE investigator (
	investigator_id INTEGER NOT NULL,
	player_id INTEGER NOT NULL,
	location INTEGER NOT NULL,
	stamina INTEGER NOT NULL,
	sanity INTEGER NOT NULL,
	focus INTEGER NOT NULL,
	speed INTEGER NOT NULL,
	sneak INTEGER NOT NULL,
	fight INTEGER NOT NULL,
	will INTEGER NOT NULL,
	lore INTEGER NOT NULL,
	luck INTEGER NOT NULL
);

-- TODO: vedere quali bonus sono possibili