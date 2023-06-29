from abc import ABC, abstractmethod

from sqlalchemy import select
from sqlalchemy.orm import Session
from bs4 import BeautifulSoup

from .parsing_methods import SeleniumParsingMethod,RequestsParsingMethod
from models.engines import engine
from models.create_schema import LinkBase, Service
from models.typical_requests import get_data_hh,get_data_sj,get_data_rr
class LinkCollectionAggregatorAbstract(ABC):
    @abstractmethod
    def getting_links(self):pass



class LinkCollectionAggregatorHH(LinkCollectionAggregatorAbstract):
    def __init__(self,subprofession):
        self._subprofession = subprofession
    def getting_links(self)->list:
        def get_numb_pages()->int:
            page = RequestsParsingMethod(self.super_url).receipt()
            soup = BeautifulSoup(page.text,"lxml")
            number_pages = soup
            return number_pages

        for i in get_numb_pages():
            page = RequestsParsingMethod(self.super_url + f"").receipt()
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
    aggregatorbehavior = {LinkCollectionAggregatorHH:get_data_hh(),LinkCollectionAggregatorSJ:get_data_sj(),LinkCollectionAggregatorRR:get_data_rr()}
    getdatabehavior = []
    def __init__(self, profession:str,subprofessions:list):
        self._profession =  profession
        self._subprofessions = subprofessions

    def get_links(self):
        for i in self.aggregatorbehavior:
           for i in self._subprofessions:
                d = i(self._subprofession).getting_links()
    def get_data(self):
        for i in self.getdatabehavior:
            pass
    def __repr__(self):
        return f"{self._profession}"


if __name__ == "__main__":
    pass