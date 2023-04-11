DROP TABLE IF EXISTS arkham_street;
CREATE TABLE arkham_street (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL
);
INSERT INTO arkham_street (name) VALUES
("northside"),
("downtown"),
("easttown"),
("rivertown"),
("merchant district"),
("miskatonic university"),
("french hill"),
("uptown"),
("southside")
;

DROP TABLE IF EXISTS street_link;
CREATE TABLE street_link (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	start_id INTEGER,
	end_id INTEGER,
	color TEXT
);
INSERT INTO street_link (start_id, end_id, color) VALUES
((SELECT id FROM arkham_street WHERE name="northside"), (SELECT id FROM arkham_street WHERE name="downtown"), "white"),
((SELECT id FROM arkham_street WHERE name="northside"), (SELECT id FROM arkham_street WHERE name="merchant district"), "black"),
((SELECT id FROM arkham_street WHERE name="downtown"), (SELECT id FROM arkham_street WHERE name="northside"), "black"),
((SELECT id FROM arkham_street WHERE name="downtown"), (SELECT id FROM arkham_street WHERE name="merchant district"), "none"),
((SELECT id FROM arkham_street WHERE name="downtown"), (SELECT id FROM arkham_street WHERE name="easttown"), "white"),
((SELECT id FROM arkham_street WHERE name="easttown"), (SELECT id FROM arkham_street WHERE name="downtown"), "black"),
((SELECT id FROM arkham_street WHERE name="easttown"), (SELECT id FROM arkham_street WHERE name="rivertown"), "white"),
((SELECT id FROM arkham_street WHERE name="rivertown"), (SELECT id FROM arkham_street WHERE name="easttown"), "black"),
((SELECT id FROM arkham_street WHERE name="rivertown"), (SELECT id FROM arkham_street WHERE name="french hill"), "white"),
((SELECT id FROM arkham_street WHERE name="rivertown"), (SELECT id FROM arkham_street WHERE name="merchant district"), "none"),
((SELECT id FROM arkham_street WHERE name="merchant district"), (SELECT id FROM arkham_street WHERE name="northside"), "white"),
((SELECT id FROM arkham_street WHERE name="merchant district"), (SELECT id FROM arkham_street WHERE name="downtown"), "none"),
((SELECT id FROM arkham_street WHERE name="merchant district"), (SELECT id FROM arkham_street WHERE name="rivertown"), "none"),
((SELECT id FROM arkham_street WHERE name="merchant district"), (SELECT id FROM arkham_street WHERE name="miskatonic university"), "black"),
((SELECT id FROM arkham_street WHERE name="miskatonic university"), (SELECT id FROM arkham_street WHERE name="merchant district"), "white"),
((SELECT id FROM arkham_street WHERE name="miskatonic university"), (SELECT id FROM arkham_street WHERE name="french hill"), "none"),
((SELECT id FROM arkham_street WHERE name="miskatonic university"), (SELECT id FROM arkham_street WHERE name="uptown"), "black"),
((SELECT id FROM arkham_street WHERE name="french hill"), (SELECT id FROM arkham_street WHERE name="miskatonic university"), "none"),
((SELECT id FROM arkham_street WHERE name="french hill"), (SELECT id FROM arkham_street WHERE name="southside"), "white"),
((SELECT id FROM arkham_street WHERE name="french hill"), (SELECT id FROM arkham_street WHERE name="rivertown"), "black"),
((SELECT id FROM arkham_street WHERE name="uptown"), (SELECT id FROM arkham_street WHERE name="miskatonic university"), "white"),
((SELECT id FROM arkham_street WHERE name="uptown"), (SELECT id FROM arkham_street WHERE name="southside"), "black"),
((SELECT id FROM arkham_street WHERE name="southside"), (SELECT id FROM arkham_street WHERE name="uptown"), "white"),
((SELECT id FROM arkham_street WHERE name="southside"), (SELECT id FROM arkham_street WHERE name="french hill"), "black")
;


DROP TABLE IF EXISTS arkham_location;
CREATE TABLE arkham_location (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	street_id INTEGER NOT NULL,
	name TEXT UNIQUE NOT NULL
);
INSERT INTO arkham_location (street_id, name) VALUES
((SELECT id FROM arkham_street WHERE name="northside"), "train station"),
((SELECT id FROM arkham_street WHERE name="northside"), "newspaper"),
((SELECT id FROM arkham_street WHERE name="northside"), "curiositie shoppe"),
((SELECT id FROM arkham_street WHERE name="downtown"), "bank of arkham"),
((SELECT id FROM arkham_street WHERE name="downtown"), "arkham asylum"),
((SELECT id FROM arkham_street WHERE name="downtown"), "independence square"),
((SELECT id FROM arkham_street WHERE name="easttown"), "hibb's roadhouse"),
((SELECT id FROM arkham_street WHERE name="easttown"), "velma's diner"),
((SELECT id FROM arkham_street WHERE name="easttown"), "police station"),
((SELECT id FROM arkham_street WHERE name="rivertown"), "graveyard"),
((SELECT id FROM arkham_street WHERE name="rivertown"), "black cave"),
((SELECT id FROM arkham_street WHERE name="rivertown"), "general store"),
((SELECT id FROM arkham_street WHERE name="merchant district"), "unvisited isle"),
((SELECT id FROM arkham_street WHERE name="merchant district"), "river docks"),
((SELECT id FROM arkham_street WHERE name="merchant district"), "the unnamable"),
((SELECT id FROM arkham_street WHERE name="miskatonic university"), "science building"),
((SELECT id FROM arkham_street WHERE name="miskatonic university"), "administration"),
((SELECT id FROM arkham_street WHERE name="miskatonic university"), "library"),
((SELECT id FROM arkham_street WHERE name="french hill"), "the witch house"),
((SELECT id FROM arkham_street WHERE name="french hill"), "silver twilight lodge"),
((SELECT id FROM arkham_street WHERE name="uptown"), "st. mary's hospital"),
((SELECT id FROM arkham_street WHERE name="uptown"), "ye olde magick shoppe"),
((SELECT id FROM arkham_street WHERE name="uptown"), "woods"),
((SELECT id FROM arkham_street WHERE name="southside"), "ma's boarding house"),
((SELECT id FROM arkham_street WHERE name="southside"), "south church"),
((SELECT id FROM arkham_street WHERE name="southside"), "historical society")
;