# from datetime import datetime
from pony.orm import PrimaryKey, Required, Optional, Database , Set


db = Database()
db.bind(provider="sqlite", filename="./database.sqlite", create_db=True)


class Uzivatel(db.Entity):
    id = PrimaryKey(int, auto=True)
    login = Required(str)
    password = Optional(str)
    email = Optional(str)
    zkracovace=Set('Zkracovac')

class Zkracovac(db.Entity):
    zkratka = PrimaryKey(str)
    url = Required(str)
    uzivatel=Optional(Uzivatel)



db.generate_mapping(create_tables=True)
