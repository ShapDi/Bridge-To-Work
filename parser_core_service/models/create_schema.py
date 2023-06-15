from datetime import date

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass




class ParserElement(Base):
    __tablename__ = "parser_element"

class StoragePattern(Base):
    __tablename__ = "storage_pattern"

class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key = True)
    name:Mapped[str] = mapped_column(String(100))
    links:Mapped[list["LinkBase"]] = relationship(
        back_populates = "service",
        cascade = "all, delete-orphan"
    )
class LinkBase(Base):
    __tablename__ = "link_base"

    id:Mapped[int] = mapped_column(primary_key = True)
    link:Mapped[str] = mapped_column(String(250))
    date:Mapped[date] = mapped_column(DateTime)
    service_id:[int] = mapped_column(ForeignKey("service.id"))
    service:Mapped["Service"] = relationship(back_populates = "link_base")



