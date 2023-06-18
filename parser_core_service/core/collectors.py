from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests
import selenium

from parsing_methods import SeleniumParsingMethod,RequestsParsingMethod


class LinkCollectionAggregatorAbstract(ABC):
    @abstractmethod
    def acquisition_links(self):pass
    @abstractmethod
    def getting_links(self):pass



class LinkCollectionAggregatorHH(LinkCollectionAggregatorAbstract):
    collections_link = []
    def __init__(self,super_url):
        self._super_url = super_url

    def acquisition_links(self,urls):
        pass
    def getting_links(self):
        page = RequestsParsingMethod(self._super_url).receipt()
        soup = BeautifulSoup(page.text,"lxml")
        number_pages =  0
        for i in number_pages:
            page = RequestsParsingMethod(self._super_url + f"").receipt()
            self.collections_link = self.collections_link + []








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