import json

from sqlalchemy.orm import Session

from engines import engine
from create_schema import Subprofessions, Professions, ParserElement, Service


with open("date\professions.json") as file:
    date = json.load(file)


with Session(engine) as ses:

        prof = Service(name = "hh")
        ses.add(prof)
        ses.commit()




