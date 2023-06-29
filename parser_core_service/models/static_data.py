import json

from sqlalchemy.orm import Session

from engines import engine
from create_schema import Subprofessions, Professions, ParserElement, Service

with open("date/professions.json") as file:
    date = json.load(file)

with Session(engine) as ses:
    def prof_data():
        for k, v in date.items():
            lis = []
            for i in v:
                s = Subprofessions(name=i)
                lis.append(s)
            d = Professions(name=k, subprofessions=lis)
            ses.add(d)
            ses.commit()


    def service_data():
        d = {"hh":"https://hh.ru/", "sj":"https://www.superjob.ru/", "rabotars":"https://www.rabota.ru/"}
        for i,n in d.items():
            n = Service(name=f"{i}",link = f"{n}")
            ses.add(n)
            ses.commit()


if __name__ == "__main__":
    prof_data()

