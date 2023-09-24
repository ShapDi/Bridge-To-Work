from sqlalchemy import select
from sqlalchemy.orm import Session
from .engines import engine

from .create_schema import ParserElement, Service, Professions, Subprofessions, SityNames,Link


def get_session():
    with Session(engine) as session:
        return session


def get_data_package(session = get_session()) -> dict:
    package = {}
    def get_service(package:dict)->dict:
        back = select(Service).except_all()
        for i in session.execute(back):
            print(i)
            package[i[1]] = {}
        return package
    def get_parsere_lement(package:dict)->dict:
        for i in list(package.keys()):
            back = select(ParserElement,Service).join_from(ParserElement,Service ).where(Service.name == i).except_all()
            package[i] = {"Xpath":{a[1]: [a[2]] for a in session.execute(back)}}
    def get_sity(package:dict)->dict:
        for i in list(package.keys()):
            back = select(SityNames).except_all()
            package[i]["sity"] = [i[1] for i in session.execute(back)]

    get_service(package)
    get_parsere_lement(package)
    get_sity(package)
    print(package)
    return package


def get_data_profession(session = get_session()):
    package = {}
    stmt = select(Professions.name, Subprofessions.name).join_from(Professions, Subprofessions).except_all()
    for i in session.execute(stmt).all():
        if package.get(i[0]) == None:
            package[i[0]] = [i[1]]
        else:
            n = package.get(i[0])
            n.append(i[1])
            package[i[0]] = n
    return package


def get_coll_prof(session = get_session()):
    stmt = select(Link.link).except_all()


if __name__ == "__main__":
    print(get_data_package())


