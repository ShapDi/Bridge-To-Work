from abc import ABC, abstractmethod

from pydantic import BaseModel

from .parsing_methods import RequestsParsingMethod



class InformationAggregatorAbstract(ABC):
    def get_name(self): pass
    def get_experience(self): pass
    def get_pay(self): pass
    def get_employment(self): pass
    def get_schedule(self): pass
    def get_text(self): pass
    def get_publication_data(self): pass
    def get_data(self): pass

class InformationAggregatorHH(InformationAggregatorAbstract):
    def __init__(self, datapackage):
        self._datapackage = datapackage
    def get_name(self): pass

    def get_experience(self): pass

    def get_pay(self): pass

    def get_employment(self): pass

    def get_schedule(self): pass

    def get_text(self): pass

    def get_publication_data(self): pass

    def get_data(self): pass

class InformationAggregatorSJ(InformationAggregatorAbstract):
    pass
class InformationAggregatorRR(InformationAggregatorAbstract):
    pass

