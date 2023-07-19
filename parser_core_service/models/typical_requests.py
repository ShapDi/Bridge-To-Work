from sqlalchemy import select
from sqlalchemy.orm import Session
from engines import engine

from create_schema import ParserElement, Service


def get_session():
    with Session(engine) as session:
        return session


def get_data_package(session = get_session()) -> dict:
    back = select(Service).except_all()
    select(ParserElement).except_all()
    package = {}
    for i in session.execute(back):
        package[i[1]] = {"god_link": i[2]}
    print(package)
    back_two = select(ParserElement).where(ParserElement.serviece == 1).except_all()
    d = list(ParserElement.__dict__["__annotations__"].keys())
    for i in session.execute(back_two):
        package["hh"][i[1]] = {d[2]: i[2], d[3]: i[3], d[4]: i[4], d[5]: i[5]}
    back_two = select(ParserElement).where(ParserElement.serviece == 2).except_all()
    for i in session.execute(back_two):
        package["sj"][i[1]] = {d[2]: i[2], d[3]: i[3], d[4]: i[4], d[5]: i[5]}
    back_two = select(ParserElement).where(ParserElement.serviece == 3).except_all()
    for i in session.execute(back_two):
        package["rabotars"][i[1]] = {d[2]: i[2], d[3]: i[3], d[4]: i[4], d[5]: i[5]}
    return package


if __name__ == "__main__":
    get_data_package()

# def get_main_link_hh(session = get_session()) -> str:
#     back = select(Service).where(Service.name == "hh")
#     link = session.scalar(back).link
#     return link
# def get_main_link_sj(session = get_session()) -> str:
#     back = select(Service).where(Service.name=="sj")
#     link = session.scalar(back).link
#     return link
# def get_main_link_rr(session = get_session()) -> str:
#     back = select(Service).where(Service.name=="rabotars")
#     link = session.scalar(back).link
#     return link
#
# def get_data_hh(session = get_session()) -> dict:
#     back = select(ParserElement).where(ParserElement.serviece == 1)
#     data_hh = session.scalar(back)
#     print(data_hh)
#
#
# def get_data_sj() -> dict:
#         pass
#
# def get_data_rr() -> dict:
#         pass
#
# get_main_link_hh()
