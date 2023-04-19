import peewee as pw
from ahc import database
from typing import Optional

class BaseModel(pw.Model):
    class Meta:
        database = database


class Location(BaseModel):
    name = pw.TextField()
    district = pw.ForeignKeyField('self', null=True, backref='locations')
    # 0: not outer world
    # 1: outer world fase 1
    # 2: outer world fase 2
    outer_world = pw.SmallIntegerField(default=0)


class StreetLink(BaseModel):
    street_from = pw.ForeignKeyField(Location, backref='out')
    street_to = pw.ForeignKeyField(Location, backref='in')
    color = pw.TextField()


class Monster(BaseModel):
    name = pw.TextField(unique=True)
    location = pw.ForeignKeyField(Location, null=True, backref='monsters')
    sign = pw.TextField()
    awareness = pw.SmallIntegerField()
    evade_check = pw.SmallIntegerField()
    horror_rating = pw.SmallIntegerField()
    horror_check = pw.SmallIntegerField()
    sanity_damage = pw.SmallIntegerField()
    combat_rating = pw.SmallIntegerField()
    toughness = pw.SmallIntegerField()
    combat_damage = pw.SmallIntegerField()


class Investigator(BaseModel):
    name = pw.TextField(unique=True)
    occupation = pw.TextField()
    home = pw.ForeignKeyField(Location)
    stamina = pw.SmallIntegerField()
    sanity = pw.SmallIntegerField()
    focus = pw.SmallIntegerField()
    speed_min = pw.SmallIntegerField(default=0) # TODO: rimuovere
    speed_max = pw.SmallIntegerField(default=0) # TODO: rimuovere
    sneak_min = pw.SmallIntegerField(default=0) # TODO: rimuovere
    sneak_max = pw.SmallIntegerField(default=0) # TODO: rimuovere
    fight_min = pw.SmallIntegerField(default=0) # TODO: rimuovere
    fight_max = pw.SmallIntegerField(default=0) # TODO: rimuovere
    will_min = pw.SmallIntegerField(default=0) # TODO: rimuovere
    will_max = pw.SmallIntegerField(default=0) # TODO: rimuovere
    lore_min = pw.SmallIntegerField(default=0) # TODO: rimuovere
    lore_max = pw.SmallIntegerField(default=0) # TODO: rimuovere
    luck_min = pw.SmallIntegerField(default=0) # TODO: rimuovere
    luck_max = pw.SmallIntegerField(default=0) # TODO: rimuovere


class Player(BaseModel):
    name = pw.TextField(unique=True)
    investigator = pw.ForeignKeyField(Investigator, backref='player')
    location = pw.ForeignKeyField(Location, backref='investigators')
    stamina = pw.SmallIntegerField(default=0) # TODO: rimuovere
    sanity = pw.SmallIntegerField(default=0) # TODO: rimuovere
    focus = pw.SmallIntegerField(default=0) # TODO: rimuovere
    speed = pw.SmallIntegerField(default=0) # TODO: rimuovere
    sneak = pw.SmallIntegerField(default=0) # TODO: rimuovere
    fight = pw.SmallIntegerField(default=0) # TODO: rimuovere
    will = pw.SmallIntegerField(default=0) # TODO: rimuovere
    lore = pw.SmallIntegerField(default=0) # TODO: rimuovere
    luck = pw.SmallIntegerField(default=0) # TODO: rimuovere
    lost = pw.BooleanField(default=False)
    blocked = pw.BooleanField(default=False)
    clues = pw.SmallIntegerField(default=0)
    money = pw.SmallIntegerField(default=0)
    gate_thropies = pw.SmallIntegerField(default=0)
    monster_thropies = pw.SmallIntegerField(default=0)


class Board(BaseModel):
    terror_track = pw.SmallIntegerField(default=0)
    max_gates = pw.SmallIntegerField(default=49)


def init_locations() -> None:
    streets = [
        ("northside",),
        ("downtown",),
        ("easttown",),
        ("rivertown",),
        ("merchant district",),
        ("miskatonic university",),
        ("french hill",),
        ("uptown",),
        ("southside",)
    ]
    outer_worlds = [
        ("another dimension", True),
        ("abyss", True),
        ("city of the great race", True),
        ("yuggoth", True),
        ("great hall of celeano", True),
        ("the dreamlands", True),
        ("plateau of leng", True),
        ("r'lyeh", True)
    ]
    with database.atomic():
        Location.insert_many(rows=streets, fields = [Location.name]).execute()
        Location.insert_many(rows=outer_worlds, fields = [Location.name, Location.outer_world]).execute()

    places = [
        (Location.get(Location.name == "northside"), "train station"),
        (Location.get(Location.name == "northside"), "newspaper"),
        (Location.get(Location.name == "northside"), "curiositie shoppe"),
        (Location.get(Location.name == "downtown"), "bank of arkham"),
        (Location.get(Location.name == "downtown"), "arkham asylum"),
        (Location.get(Location.name == "downtown"), "independence square"),
        (Location.get(Location.name == "easttown"), "hibb's roadhouse"),
        (Location.get(Location.name == "easttown"), "velma's diner"),
        (Location.get(Location.name == "easttown"), "police station"),
        (Location.get(Location.name == "rivertown"), "graveyard"),
        (Location.get(Location.name == "rivertown"), "black cave"),
        (Location.get(Location.name == "rivertown"), "general store"),
        (Location.get(Location.name == "merchant district"), "unvisited isle"),
        (Location.get(Location.name == "merchant district"), "river docks"),
        (Location.get(Location.name == "merchant district"), "the unnamable"),
        (Location.get(Location.name == "miskatonic university"), "science building"),
        (Location.get(Location.name == "miskatonic university"), "administration"),
        (Location.get(Location.name == "miskatonic university"), "library"),
        (Location.get(Location.name == "french hill"), "the witch house"),
        (Location.get(Location.name == "french hill"), "silver twilight lodge"),
        (Location.get(Location.name == "uptown"), "st. mary's hospital"),
        (Location.get(Location.name == "uptown"), "ye olde magick shoppe"),
        (Location.get(Location.name == "uptown"), "woods"),
        (Location.get(Location.name == "southside"), "ma's boarding house"),
        (Location.get(Location.name == "southside"), "south church"),
        (Location.get(Location.name == "southside"), "historical society")
    ]
    links = [
        (Location.get(Location.name == "northside"), Location.get(Location.name == "downtown"), "white"),
        (Location.get(Location.name == "northside"), Location.get(Location.name == "merchant district"), "black"),
        (Location.get(Location.name == "downtown"), Location.get(Location.name == "northside"), "black"),
        (Location.get(Location.name == "downtown"), Location.get(Location.name == "merchant district"), "none"),
        (Location.get(Location.name == "downtown"), Location.get(Location.name == "easttown"), "white"),
        (Location.get(Location.name == "easttown"), Location.get(Location.name == "downtown"), "black"),
        (Location.get(Location.name == "easttown"), Location.get(Location.name == "rivertown"), "white"),
        (Location.get(Location.name == "rivertown"), Location.get(Location.name == "easttown"), "black"),
        (Location.get(Location.name == "rivertown"), Location.get(Location.name == "french hill"), "white"),
        (Location.get(Location.name == "rivertown"), Location.get(Location.name == "merchant district"), "none"),
        (Location.get(Location.name == "merchant district"), Location.get(Location.name == "northside"), "white"),
        (Location.get(Location.name == "merchant district"), Location.get(Location.name == "downtown"), "none"),
        (Location.get(Location.name == "merchant district"), Location.get(Location.name == "rivertown"), "none"),
        (Location.get(Location.name == "merchant district"), Location.get(Location.name == "miskatonic university"), "black"),
        (Location.get(Location.name == "miskatonic university"), Location.get(Location.name == "merchant district"), "white"),
        (Location.get(Location.name == "miskatonic university"), Location.get(Location.name == "french hill"), "none"),
        (Location.get(Location.name == "miskatonic university"), Location.get(Location.name == "uptown"), "black"),
        (Location.get(Location.name == "french hill"), Location.get(Location.name == "miskatonic university"), "none"),
        (Location.get(Location.name == "french hill"), Location.get(Location.name == "southside"), "white"),
        (Location.get(Location.name == "french hill"), Location.get(Location.name == "rivertown"), "black"),
        (Location.get(Location.name == "uptown"), Location.get(Location.name == "miskatonic university"), "white"),
        (Location.get(Location.name == "uptown"), Location.get(Location.name == "southside"), "black"),
        (Location.get(Location.name == "southside"), Location.get(Location.name == "uptown"), "white"),
        (Location.get(Location.name == "southside"), Location.get(Location.name == "french hill"), "black")
    ]
    with database.atomic():
        Location.insert_many(rows=places, fields=[Location.district, Location.name]).execute()
        StreetLink.insert_many(rows=links, fields=[StreetLink.street_from, StreetLink.street_to, StreetLink.color]).execute()


def init_investigators() -> None:
    investigators = [
        ("Amanda Sharpe", "student", Location.get(Location.name == "bank of arkham"), 5, 5, 3),
        ("'Ashcan' Pete", "drifter", Location.get(Location.name == "river docks"), 6, 4, 1),
        ("Bob Jenkins", "salesman", Location.get(Location.name == "general store"), 4, 6, 1)
    ]
    with database.atomic():
        Investigator.insert_many(rows=investigators,fields=[
            Investigator.name,
            Investigator.occupation,
            Investigator.home,
            Investigator.stamina,
            Investigator.sanity,
            Investigator.focus
        ]).execute()

def init_db(database:pw.SqliteDatabase):
    database.connect()
    tables : dict[BaseModel, Optional[callable]] = {
        Location: init_locations,
        StreetLink: None,
        Monster: None,
        Investigator: init_investigators,
        Player: None,
        Board: None
    }
    database.create_tables(tables.keys())
    for table, initter in tables.items():
        if initter and len(table.select()) == 0:
            initter()