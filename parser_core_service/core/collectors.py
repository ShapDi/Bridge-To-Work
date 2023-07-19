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
        colections = []
        def get_numb_pages()->int:
            page = RequestsParsingMethod(self._aggregator_link + f"/search/vacancy?text={self._subprofession}").receipt()
            soup = BeautifulSoup(page.text,"lxml")
            number_pages = int(soup.find("div",class_ = "bloko-gap bloko-gap_top").find_all("span")[-1].text)
            return number_pages

        for i in get_numb_pages():
            page = RequestsParsingMethod(self._aggregator_link + f"?text=pathon&salary=&page={i}&ored_clusters=true").receipt()
            soup = BeautifulSoup(page.text, "lxml")
            link = soup.find_all("a", class_ = "serp-item__title")
            colections.append(link)

        print(colections)


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
        list_link_hh = {}
        list_link_sj = {}
        list_link_rr = {}
        for i in self._subprofessions:
                hh = self.aggregatorbehavior.keys()[0](i,self.aggregatorbehavior.values()[0][0],self.aggregatorbehavior.values()[0][1]).getting_links()
                sj = self.aggregatorbehavior.keys()[1](i,self.aggregatorbehavior.values()[1][0],self.aggregatorbehavior.values()[1][1]).getting_links()
                rr = self.aggregatorbehavior.keys()[2](i,self.aggregatorbehavior.values()[2][0],self.aggregatorbehavior.values()[2][1]).getting_links()
                list_link_hh[i] = hh
                list_link_sj[i] = sj
                list_link_rr[i] = rr
        return list_link_hh, list_link_sj, list_link_rr

    def get_data(self):
        for databehavior_type,data_search in self.getdatabehavior.items():
            for i in self._subprofessions:
                d = databehavior_type(i, data_search)
    def __repr__(self):
        return f"{self._profession}"


if __name__ == "__main__":
    pass