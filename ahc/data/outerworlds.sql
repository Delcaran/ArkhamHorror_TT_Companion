DROP TABLE IF EXISTS outer_world;
CREATE TABLE outer_world (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL
);

INSERT INTO outer_world (name)
VALUES
("another dimension"),
("abyss"),
("city of the great race"),
("yuggoth"),
("great hall of celeano"),
("the dreamlands"),
("plateau of leng"),
("r'lyeh")
;
