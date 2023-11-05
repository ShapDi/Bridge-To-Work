from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

if __name__ == '__main__':
    from engines import engine
else:
    from engines import engine
class Base(DeclarativeBase):
    pass

class ParserElement(Base):
    __tablename__ = "parser_element"
    id: Mapped[int] = mapped_column(primary_key=True)
    name_element: Mapped[str] = mapped_column(String(20))
    Xpath: Mapped[str]
    serviece: Mapped[int] = mapped_column(ForeignKey("services.id"))


class SityNames(Base):
    __tablename__ = "cities"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))


class Service(Base):
    __tablename__ = "services"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

class Link(Base):
    __tablename__ = "links"
    id: Mapped[int] = mapped_column(primary_key = True)
    link: Mapped[str] = mapped_column(String(1000))
    subprofessions: Mapped[int] = mapped_column(ForeignKey("subprofessions.id"))
    сity: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
class Vacancy(Base):
    __tablename__ = "vacancys"
    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(40))
    link: Mapped[str] = mapped_column(String(255))
    experience:Mapped[str] = mapped_column(String(30))
    pay:Mapped[int]
    country:Mapped[str] = mapped_column(String(50))
    сity:Mapped[int] = mapped_column(ForeignKey("cities.id"))
    employment:Mapped[str] = mapped_column(String(50))
    schedule:Mapped[str] = mapped_column(String(50))
    Text:Mapped[str]
    subprofession_id: Mapped[int] = mapped_column(ForeignKey("subprofessions.id"))
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))






class Subprofessions(Base):
    __tablename__ = "subprofessions"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    profession_id: Mapped[int] = mapped_column(ForeignKey("professions.id"))
    profession: Mapped["Professions"] = relationship(back_populates="subprofessions")


class Professions(Base):
    __tablename__ = "professions"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    subprofessions: Mapped[list["Subprofessions"]] = relationship(back_populates="profession")


# class DeclensionsСity(Base):
#     __tablename__ = "declensions_сity"
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(255))
#     сity_id: Mapped[int] = mapped_column(ForeignKey("сity_collection.id"))


def main():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()
