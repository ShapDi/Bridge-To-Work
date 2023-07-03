from sqlalchemy import select
from sqlalchemy.orm import Session
from engines import engine

from create_schema import ParserElement, Service

def get_session():
    with Session(engine) as session:
        return session

class TypicalRequests():
    def __init__(self, classORM):
        self._classORM = classORM



def get_main_link_hh(session = get_session()) -> str:
    back = select(Service).where(Service.name == "hh")
    link = session.scalar(back).link
    return link
def get_main_link_sj(session = get_session()) -> str:
    back = select(Service).where(Service.name=="sj")
    link = session.scalar(back).link
    return link
def get_main_link_rr(session = get_session()) -> str:
    back = select(Service).where(Service.name=="rabotars")
    link = session.scalar(back).link
    return link

def get_data_hh(session = get_session()) -> dict:
    back = select(ParserElement).where(ParserElement.serviece == 1)
    data_hh = session.scalar(back)
    print(data_hh)


def get_data_sj() -> dict:
        pass

def get_data_rr() -> dict:
        pass

get_main_link_hh()