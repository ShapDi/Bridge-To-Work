from abc import ABC, abstractmethod

from .parsing_methods import RequestsParsingMethod

class InformationAggregatorAbstract(ABC):
    @abstractmethod
    def get_text(self): pass

    @abstractmethod
    def get_salary(self): pass


class InformationAggregatorHH(InformationAggregatorAbstract):
    pass
