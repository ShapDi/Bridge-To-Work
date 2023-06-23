import json

from sqlalchemy.orm import Session

from engines import engine
from create_schema import Subprofessions, Professions, ParserElement, Service


with open("date\professions.json") as file:
    date = json.load(file)


with Session(engine) as ses:
    def prof_data():
        for k,v in date.items():
            lis = []
            for i in v:
                s = Subprofessions(name = i)
                lis.append(s)
            d = Professions(name = k, subprofessions = lis)
            ses.add(d)
            ses.commit()
    def service_data():
        d = ["hh","sj","rabotars"]
        for i in d:
            n = Service(name = f"{i}")
            ses.add(n)
            ses.commit()




