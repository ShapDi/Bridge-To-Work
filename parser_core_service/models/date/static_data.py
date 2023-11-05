import json

from sqlalchemy.orm import Session

from models.engines import engine
from models.create_schema import Subprofessions, Professions, ParserElement, Service, SityNames

with open("professions.json") as file:
    date = json.load(file)

with open("vacancys_data.json") as vac:
    data_vac = json.load(vac)

def get_session():
    with Session(engine) as session:
        return session

def prof_data(session = get_session()):
    for k, v in date.items():
        lis = []
        for i in v:
            s = Subprofessions(name=i)
            lis.append(s)
        d = Professions(name=k, subprofessions=lis)
        session.add(d)
        session.commit()

def service_data(session = get_session()):
    d = {"hh":"https://hh.ru/", "sj":"https://www.superjob.ru/", "rr":"https://www.rabota.ru/"}
    for i,n in d.items():
        n = Service(name=f"{i}")
        session.add(n)
        session.commit()
def get_data_search_links(session = get_session()):
    link_hh = ParserElement(name_element = "link",  Xpath = """/html/body/div/div/div/div/div/div/div/main/div/div/div/div/div/div/h3/span/a/@href""", serviece  = 1)
    link_sj = ParserElement(name_element="link",
                      Xpath="""/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/span/a/@href""",
                      serviece=2)
    link_rru = ParserElement(name_element="link",
                      Xpath="""/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/main/div/div/div/div/div/article/div/div/div[1]/header/h3/a/@href""",
                      serviece=3)

    session.add(link_hh)
    session.add(link_sj)
    session.add(link_rru)
    session.commit()

def get_data_sity(session = get_session()):
    sity_col = ["Москва","Санкт-Петербург","Новосибирск","Екатеринбург","Казань","Нижний Новгород","Челябинск",
                "Самара","Уфа","Ростов-на-Дону","Омск","Красноярск","Воронеж","Пермь","Волгоград"]
    for i in sity_col:
        d = SityNames(name = i)
        session.add(d)
    session.commit()


def add_job_search_data(session = get_session()):
    for name,xpath in data_vac['hh'].items():
        hh = ParserElement(name_element = name, Xpath = xpath, serviece = 1)
        session.add(hh)
    for name,xpath in data_vac['sj'].items():
        sj = ParserElement(name_element = name, Xpath = xpath, serviece = 2)
        session.add(sj)
    for name,xpath in data_vac['rr'].items():
        rr = ParserElement(name_element = name, Xpath = xpath, serviece = 3)
        session.add(rr)
    session.commit()

# if __name__ == "__main__":
#     service_data()
#     prof_data()
#     get_data_search_links()
#     get_data_sity()
#     add_job_search_data()
#
#


