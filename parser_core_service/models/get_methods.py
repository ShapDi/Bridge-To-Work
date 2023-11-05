import json
import redis

from sqlalchemy import select
from sqlalchemy.orm import Session
from engines import engine

from create_schema import ParserElement, Service, Professions, Subprofessions, SityNames, Link


def get_session():
    with Session(engine) as session:
        return session


def get_data_package(session = get_session()) -> dict:
    package = {}

    def get_service(package: dict) -> dict:
        back = select(Service).except_all()
        for i in session.execute(back):
            print(i)
            package[i[1]] = {}

        return package

    def get_parsere_lement(package: dict) -> dict:
        for i in list(package.keys()):
            back = select(ParserElement, Service).join_from(ParserElement, Service).where(
                Service.name == i).except_all()
            package[i] = {"Xpath": {a[1]: [a[2]] for a in session.execute(back)}}

    def get_sity(package: dict) -> dict:
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


def link_vac(subprofession, session = get_session()):
    stmt = select(Link.link).join_from(Link, Subprofessions).where(Subprofessions.name == subprofession).except_all()
    print(session.execute(stmt).all())


def checking_link(links, session = get_session()):
    exists_criteria = (
        select(Link.link).
        where(Link.link == links).
        exists()
    )
    stmt = select(Link).where(exists_criteria)
    print(session.execute(stmt).scalar())


def get_link(session = get_session()):
    links = select(Link.link).except_all()
    for link in session.execute(links).all():
        yield link


def get_coll_prof(session = get_session()):
    stmt = select(Professions).except_all()


def get_links_hh(session = get_session()):
    links = select(Link.link, Service.id, Service.name).join_from(Link, Service).where(Service.name == 'hh')
    for link in session.execute(links).all():
        yield link


def get_links_sj(session = get_session()):
    links = select(Link.link, Service.id, Service.name).join_from(Link, Service).where(Service.name == 'sj')
    for link in session.execute(links).all():
        yield link


def get_links_rr(session = get_session()):
    links = select(Link.link, Service.id, Service.name).join_from(Link, Service).where(Service.name == 'rr')
    for link in session.execute(links).all():
        yield link


def get_job_search_data(session = get_session()):
    with redis.Redis() as cache:
        job_search_data = cache.get('job_search_data')
        if job_search_data is not None:
            return json.loads(job_search_data)
        stmt = select(ParserElement.name_element, ParserElement.Xpath, Service.id, Service.name).join_from(
            ParserElement, Service).except_all()
        job_search_data_collection = {}
        for data in session.execute(stmt).all():
            if data.name not in job_search_data_collection:
                job_search_data_collection[data.name] = {data.name_element:{"Xpath": data.Xpath}}
            else:
                job_search_data_collection[data.name][data.name_element] = {"Xpath": data.Xpath}
        cache.set('job_search_data', json.dumps(job_search_data_collection))
        return json.loads(cache.get('job_search_data'))


if __name__ == "__main__":
    # link_vac('Аудитор')
    # checking_link('https://www.superjob.ru/vakansii/specialist-ekonomicheskoj-bezopasnosti-44526724.html')
    print(get_job_search_data())
