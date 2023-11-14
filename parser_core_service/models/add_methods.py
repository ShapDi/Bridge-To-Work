from sqlalchemy.orm import Session

from models.create_schema import Link, Vacancy
from .engines import engine

def get_session():
    with Session(engine) as session:
        return session

def add_link(link,sity,subprofessions,service_id, session = get_session()):
    link = Link(link = link, сity = sity, subprofessions = subprofessions,service_id = service_id)
    session.add(link)
    session.commit()

def add_vacancy(session = get_session()):
    vacancy = Vacancy(link = '', сity = '', service_id = '', date = '')