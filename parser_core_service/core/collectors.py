from abc import ABC, abstractmethod
from .parsing_methods import RequestsParsingMethod
import logging


class LinkCollectionAggregatorAbstract(ABC):
    @abstractmethod
    def getting_links(self): pass


class LinkCollectionAggregatorHH(LinkCollectionAggregatorAbstract):
    def __init__(self, subprofession: str, datapackage: dict):
        self._subprofession = subprofession
        self._datapackage = datapackage
        element = []

    # Данная функция должна возращать словарь с ключем hh и списком
    def getting_links(self) -> dict:
        links = []
        col_page = RequestsParsingMethod(url=f"https://hh.ru/search/vacancy?text=python",
                                         elements=[f"""{self._datapackage['page_number']['Xpath']}"""]).get_element()
        for i in range(1,int(col_page[0])+1):
            element = RequestsParsingMethod(url=f"https://hh.ru/search/vacancy?text=python&page={i}",
                                            elements=[f"""{self._datapackage['link']['Xpath']}"""]).get_element()
            links = links + element
        return links


class LinkCollectionAggregatorSJ(LinkCollectionAggregatorAbstract):
    def __init__(self, subprofession: str, datapackage: dict):
        self._subprofession = subprofession
        self._datapackage = datapackage

    pass


class LinkCollectionAggregatorRR(LinkCollectionAggregatorAbstract):
    def __init__(self, subprofession: str, datapackage: dict):
        self._subprofession = subprofession
        self._datapackage = datapackage


class InformationAggregatorAbstract(ABC):
    @abstractmethod
    def get_text(self): pass

    @abstractmethod
    def get_salary(self): pass


class InformationAggregatorHH(InformationAggregatorAbstract):
    pass


class Aggregator():
    SET_aggregatorbehavior = [LinkCollectionAggregatorHH, LinkCollectionAggregatorSJ, LinkCollectionAggregatorSJ]
    SET_infoaggregatorbehavior = []
    SET_aggregators = {}

    def __init__(self, profession: str, subprofessions: list, datapackage: dict):
        self._profession = profession
        self._subprofessions = subprofessions
        self._datapackage = datapackage

    def initialization_agregators(self):
        for i in self._subprofessions:
            self.SET_aggregators[i] = [
                LinkCollectionAggregatorHH(i, self._datapackage.get("hh")),
                # LinkCollectionAggregatorSJ(i,self._datapackage),
                # LinkCollectionAggregatorRR(i,self._datapackage),
            ]

    def get_links(self) -> dict:
        link_colectors = {}
        for i, n in self.SET_aggregators.items():
            resalt_serch = list(map(lambda i: i.getting_links(), n))
            link_colectors[i] = resalt_serch
            logging.warning(link_colectors)
        return link_colectors

    def get_info(self):
        pass

    def __repr__(self):
        return f"{self._profession}"


if __name__ == "__main__":
    pass
