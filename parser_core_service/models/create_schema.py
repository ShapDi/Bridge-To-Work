from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from engines import engine
class Base(DeclarativeBase):
    pass


class ParserElement(Base):
    __tablename__ = "parser_element"
    id: Mapped[int] = mapped_column(primary_key = True)
    name_element: Mapped[str] = mapped_column(String(20))
    tag: Mapped[str] = mapped_column(String(20))
    class_html: Mapped[str] = mapped_column(String(300))
    CSS_selector: Mapped[str | None]
    Xpath: Mapped[str | None]
    serviece: Mapped[int] = mapped_column(ForeignKey("services.id"))


class Service(Base):
    __tablename__ = "services"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(100))
    link: Mapped[str] = mapped_column(String(100))


class LinkBase(Base):
    __tablename__ = "link_base"
    id: Mapped[int] = mapped_column(primary_key = True)
    link: Mapped[str] = mapped_column(String(255))
    subprofession_id: Mapped[int] = mapped_column(ForeignKey("subprofessions.id"))
    date: Mapped[datetime] = mapped_column(DateTime(timezone = True), server_default = func.now())
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))

class Subprofessions(Base):
    __tablename__ = "subprofessions"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(255))
    profession_id: Mapped[int] = mapped_column(ForeignKey("professions.id"))
    profession: Mapped["Professions"] = relationship(back_populates = "subprofessions")
class Professions(Base):
    __tablename__ = "professions"
    id: Mapped[int] = mapped_column(primary_key = True,autoincrement = True)
    name: Mapped[str] = mapped_column(String(255))
    subprofessions: Mapped[list["Subprofessions"]] = relationship(back_populates = "profession")







def main():
    Base.metadata.create_all(bind = engine)
    

if __name__ == "__main__":
    main()
