from abc import ABC, abstractmethod
from sqlalchemy import select
from sqlalchemy.orm import Session
from bs4 import BeautifulSoup
import requests
import selenium

from models.create_schema import Link
from parsing_methods import SeleniumParsingMethod,RequestsParsingMethod

from models.engines import engine


class LinkCollectionAggregatorAbstract(ABC):
    @abstractmethod
    def acquisition_links(self):pass
    @abstractmethod
    def getting_links(self):pass



class LinkCollectionAggregatorHH(LinkCollectionAggregatorAbstract):
    collections_link = []
    def __init__(self,super_url):
        self._super_url = super_url

    def acquisition_links(self):
        with Session(engine) as ses:
            for i in self.collections_link:
                stmt = select(Link.link == f"{i}")
                rez = ses.scalar(stmt)
                if rez == []:
                    continue
                else:
                    pass

    def getting_links(self):
        def get_numb_pages()->int:
            page = RequestsParsingMethod(self._super_url).receipt()
            soup = BeautifulSoup(page.text,"lxml")
            number_pages = soup
            return number_pages

        for i in get_numb_pages():
            page = RequestsParsingMethod(self._super_url + f"").receipt()
            self.collections_link = self.collections_link + []
        self.acquisition_links()


class LinkCollectionAggregatorSJ(LinkCollectionAggregatorAbstract):
    pass

class LinkCollectionAggregatorRR(LinkCollectionAggregatorAbstract):
    pass

class InformationAggregatorAbstract(ABC):
    @abstractmethod
    def get_text(self):pass

    @abstractmethod
    def get_salary(self):pass



class Aggregator():
    def __init__(self, aggregatorbehavior:LinkCollectionAggregatorAbstract):
        self._aggregatorbehavior = aggregatorbehavior



if __name__ == "__main__":
    pass