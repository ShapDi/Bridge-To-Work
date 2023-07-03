from abc import ABC, abstractmethod

from sqlalchemy import select
from sqlalchemy.orm import Session
from bs4 import BeautifulSoup

from .parsing_methods import SeleniumParsingMethod,RequestsParsingMethod
from models.engines import engine
from models.create_schema import LinkBase, Service
from models.typical_requests import get_main_link_hh,get_main_link_sj,get_main_link_rr, get_data_hh,get_data_sj,get_data_rr
class LinkCollectionAggregatorAbstract(ABC):
    @abstractmethod
    def getting_links(self):pass



class LinkCollectionAggregatorHH(LinkCollectionAggregatorAbstract):
    def __init__(self,subprofession:str,aggregator_link:str,data_link:dict):
        self._subprofession = subprofession
        self._aggregator_link = aggregator_link
        self._data_link = data_link
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
    aggregatorbehavior = {LinkCollectionAggregatorHH:[get_main_link_hh(),],LinkCollectionAggregatorSJ:[get_main_link_sj()],LinkCollectionAggregatorRR:[get_main_link_rr()]}
    getdatabehavior = {}
    def __init__(self, profession:str,subprofessions:list):
        self._profession =  profession
        self._subprofessions = subprofessions

    def get_links(self):
        for aggregator_type,data_search in self.aggregatorbehavior.items():
           for i in self._subprofessions:
                d = aggregator_type(i,data_search[0],data_search[1]).getting_links()
    def get_data(self):
        for databehavior_type,data_search in self.getdatabehavior.items():
            for i in self._subprofessions:
                d = databehavior_type(i, data_search)
    def __repr__(self):
        return f"{self._profession}"


if __name__ == "__main__":
    pass