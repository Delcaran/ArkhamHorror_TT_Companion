DROP TABLE IF EXISTS investigator;
CREATE TABLE investigator (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL,
	occupation TEXT NOT NULL,
	home TEXT NOT NULL, -- deve diventare un ID a location
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

INSERT INTO investigator (name, occupation, home, stamina, sanity, focus, speed_min, speed_max, sneak_min, sneak_max, fight_min, fight_max, will_min, will_max, lore_min, lore_max, luck_min, luck_max)
VALUES
("Amanda Sharpe", "student", "bank of arkham", 5, 5, 3, 0,0,0,0,0,0,0,0,0,0,0,0),
("'Ashcan' Pete", "drifter", "river docks", 6, 4, 1, 0,0,0,0,0,0,0,0,0,0,0,0),
("Bob Jenkins", "salesman", "general store", 4, 6, 1, 0,0,0,0,0,0,0,0,0,0,0,0)
;
