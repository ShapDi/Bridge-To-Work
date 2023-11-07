from abc import ABC, abstractmethod
from .parsing_methods import RequestsParsingMethod

class Red:
    def __init__(self, text):
        self._text = text

    def red_link(self):
        return str(self._text).split("?")[0]


class LinkCollectionAggregatorAbstract(ABC):
    @abstractmethod
    def getting_links(self): pass

# class LinkCollectionAggregatorHH(LinkCollectionAggregatorAbstract):
#     def __init__(self, subprofession: str, datapackage: dict):
#         self._subprofession = subprofession
#         self._datapackage = datapackage
#
#     @staticmethod
#     def pagination_check():
#         for i in range(1, 100):
#             page = i
#             yield page
#
#     def getting_links(self) -> dict:
#         for sity in self._datapackage["sity"]:
#             links = {}
#             col = []
#             for i in self.pagination_check():
#                 element = RequestsParsingMethod(
#                     url=f"https://hh.ru/search/vacancy?text={self._subprofession}+{sity}&page={i}",
#                     elements=self._datapackage['Xpath']['link']).get_element()
#                 col = col + element
#                 if element != "Нет элементов":
#                     break
#             links[sity] = col
#             yield links

class LinkCollectionAggregatorHH(LinkCollectionAggregatorAbstract):
    def __init__(self, request, datalink):
        self._request = request
        self._datalink = datalink

    @staticmethod
    def pagination_check():
        for i in range(1, 100):
            page = i
            yield page
    def getting_links(self):
        coll = []
        for i in self.pagination_check():
            element = RequestsParsingMethod(
            url=f"https://hh.ru/search/vacancy?text={self._request}&page={i}",
            elements=self._datalink.hh).get_element()
            coll= coll + element
            if element != "Нет элементов":
                break
        coll = [Red(i.get('href')).red_link() for i in coll]
        print(coll)
        return coll

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
            yield links
