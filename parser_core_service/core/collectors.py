from abc import ABC, abstractmethod

import requests
import selenium



class LinkCollectionAggregatorAbstract(ABC):
    @abstractmethod
    def getting_links(self):pass

    @abstractmethod
    def acquisition_links(self):pass

class LinkCollectionAggregatorHH(LinkCollectionAggregatorAbstract):
    pass

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