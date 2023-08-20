from sqlalchemy.orm import Session

from .create_schema import Link
from .engines import engine

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
    def get_idsevices(name_service):
        col_service = {"hh": 1,"sj":2,"rabotars":3}
        return col_service[f"{name_service}"]

    def saving_link(self,session = get_session()):
        print(self._data)
        sub_pg = list(self._data.keys())[0]
        print(sub_pg)
        sity = list(self._data[f"{sub_pg}"].keys())[0]
        print(sub_pg)
        for sevice,links in self._data[f'{sub_pg}'][f'{sity}'].items() :
            for link in links:
                link = Link(subprofessions = sub_pg, сity = sity,link = link, service_id = self.get_idsevices(sevice))
                session.add(link)
        session.commit()


