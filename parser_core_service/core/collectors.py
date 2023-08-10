from abc import ABC, abstractmethod
from .parsing_methods import RequestsParsingMethod
import logging

class Сleaner():
    def __init__(self, mass_col_old, mass_col_new):
        self._mass_col_old = mass_col_old
        self._mass_col_new = mass_col_new

    def proverca(self):
        pass

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
        links = {}
        for sity in self._datapackage["sity"]:
            col_page = RequestsParsingMethod(url=f"https://hh.ru/search/vacancy?text={self._subprofession}+{sity}",
                                             elements=self._datapackage['Xpath']['page_number']).get_element()
            if col_page[0] == "Нет элементов":
                col_page[0] = 1
            col =[]
            for i in range(1, int(col_page[0])+1):
                element = RequestsParsingMethod(url=f"https://hh.ru/search/vacancy?text={self._subprofession}+{sity}&page={i}",
                                                elements=self._datapackage['Xpath']['link']).get_element()
                col = col + element
            links[sity] = col
        logging.warning(links)
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

    def get_ready_data(self):
        if not self.SET_aggregators:
            self.initialization_agregators()
            links = self.get_links()
        else:
            links = self.get_links()


    def __repr__(self):
        return f"{self._profession}"


if __name__ == "__main__":
    pass
