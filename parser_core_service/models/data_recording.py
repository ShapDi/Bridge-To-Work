from sqlalchemy.orm import Session

from .create_schema import Link
from .engines import engine
from sqlalchemy import select
from .create_schema import Service,SityNames,Subprofessions


def get_session():
    with Session(engine) as session:
        return session

class DataRecording():
    def __init__(self, data):
        self._data = data

    @staticmethod
    def get_session():
        with Session(engine) as session:
            return session
    @staticmethod
    def get_sevicesid(name_service,session = get_session()):
        stmt = select(Service).where(Service.name == name_service)
        service_id = (session.scalars(stmt).one()).id
        return service_id
    @staticmethod
    def get_sityid(name_sity,session = get_session()):
        stmt = select(SityNames).where(SityNames.name == name_sity)
        sity_id = (session.scalars(stmt).one()).id
        return sity_id
    @staticmethod
    def get_subprofessionsid(name_subprofessions,session = get_session()):
        stmt = select(Subprofessions).where(Subprofessions.name == name_subprofessions)
        subprofessions_id = (session.scalars(stmt).one()).id
        return subprofessions_id
    def saving_link(self,session = get_session()):
        sub_pg = list(self._data.keys())[0]
        sity = list(self._data[f"{sub_pg}"].keys())[0]
        for sevice,links in self._data[f'{sub_pg}'][f'{sity}'].items():
            for link in links[0]:
                link = Link(subprofessions = self.get_subprofessionsid(sub_pg), сity = self.get_sityid(sity),link = link, service_id = self.get_sevicesid(sevice))
                session.add(link)
        session.commit()


