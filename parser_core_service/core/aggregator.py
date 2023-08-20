from abc import ABC, abstractmethod

from core.accumulation_links import LinkCollectionAggregatorHH, LinkCollectionAggregatorSJ, LinkCollectionAggregatorRR
from .parsing_methods import RequestsParsingMethod
import logging


class Сleaner():
    def __init__(self, mass_col_old, mass_col_new):
        self._mass_col_old = mass_col_old
        self._mass_col_new = mass_col_new

    def proverca(self):
        pass


class Aggregator():
    SET_aggregatorbehavior = [LinkCollectionAggregatorHH, LinkCollectionAggregatorSJ, LinkCollectionAggregatorRR]
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
            link_colectors = {f"{i}":{}}
            logging.warning(link_colectors)
            for num_sity in range(1,len(self._datapackage["hh"]["sity"])):
                hh = next(n[0])
                sj = next(n[1])
                rr = next(n[2])
                link_colectors[i] = {f"{list(hh.keys())[0]}":{"hh":list(hh.values())}}
                logging.warning(link_colectors)
                # link_colectors = {f"{i}":[n[0],n[1],n[2]]}
                logging.warning(link_colectors)
            yield link_colectors

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
