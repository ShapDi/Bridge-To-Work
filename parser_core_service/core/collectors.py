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

    @staticmethod
    def pagination_check():
        for i in range(1, 100):
            page = i
            yield page

    def getting_links(self) -> dict:
        for sity in self._datapackage["sity"]:
            links = {}
            col = []
            for i in self.pagination_check():
                element = RequestsParsingMethod(
                    url=f"https://hh.ru/search/vacancy?text={self._subprofession}+{sity}&page={i}",
                    elements=self._datapackage['Xpath']['link']).get_element()
                col = col + element
                if element != "Нет элементов":
                    break
            links[sity] = col
            logging.warning(links)
            yield links


class LinkCollectionAggregatorSJ(LinkCollectionAggregatorAbstract):
    def __init__(self, subprofession: str, datapackage: dict):
        self._subprofession = subprofession
        self._datapackage = datapackage

    @staticmethod
    def pagination_check():
        for i in range(1, 100):
            page = i
            yield page

    def getting_links(self) -> dict:
        for sity in self._datapackage["sity"]:
            links = {}
            col = []
            for i in self.pagination_check():
                element = RequestsParsingMethod(
                    url=f"https://www.superjob.ru/vacancy/search/?keywords={self._subprofession}+{sity}&page={i}",
                    elements=self._datapackage['Xpath']['link']).get_element()
                col = col + [f"https://www.superjob.ru{i}" for i in  element]
                if element != "Нет элементов":
                    break
            links[sity] = col
            logging.warning(links)
            yield links


class LinkCollectionAggregatorRR(LinkCollectionAggregatorAbstract):
    def __init__(self, subprofession: str, datapackage: dict):
        self._subprofession = subprofession
        self._datapackage = datapackage

    @staticmethod
    def pagination_check():
        for i in range(1, 100):
            page = i
            yield page

    def getting_links(self) -> dict:
        for sity in self._datapackage["sity"]:
            links = {}
            col = []
            for i in self.pagination_check():
                element = RequestsParsingMethod(
                    url=f"https://www.rabota.ru/vacancy/?query={self._subprofession}+{sity}&page={i}",
                    elements=self._datapackage['Xpath']['link']).get_element()
                col = col + [f"https://www.rabota.ru{i}" for i in element]
                if element != "Нет элементов":
                    break
            links[sity] = col
            logging.warning(links)
            yield links


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
                LinkCollectionAggregatorHH(i, self._datapackage.get("hh")).getting_links(),
                LinkCollectionAggregatorSJ(i, self._datapackage.get("sj")).getting_links(),
                LinkCollectionAggregatorRR(i, self._datapackage.get("rabotars")).getting_links(),
            ]

    def get_links(self):
        for i, n in self.SET_aggregators.items():
            logging.warning(n)
            link_colectors = {f"{i}":{}}
            for num_sity in range(1,len(self._datapackage["hh"]["sity"])):
                hh = next(n[0])
                sj = next(n[1])
                rr = next(n[2])
                link_colectors[i] = {f"{list(hh.keys())[0]}":{"hh":list(hh.values())}}
                logging.warning(link_colectors)
        link_colectors = {f"{i}":[n[0],n[1],n[2]]}
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
