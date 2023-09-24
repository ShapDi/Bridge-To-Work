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
    def get_name(self):
        name_element = self._datapackage['name']

    def get_experience(self):
        experience_element = self._datapackage['experience']

    def get_pay(self):
        pay_element = self._datapackage['pay']

    def get_employment(self):
        employment_element = self._datapackage['employment']

    def get_schedule(self):
        schedule_element = self._datapackage['schedule']
    def get_text(self):
        schedule_text = self._datapackage['text']

    def get_publication_data(self):
        schedule_publication_data = self._datapackage['text']

    def get_city(self): pass


    def get_data(self): pass

class InformationAggregatorSJ(InformationAggregatorAbstract):
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

class InformationAggregatorRR(InformationAggregatorAbstract):
    def __init__(self, datapackage):
        self._datapackage = datapackage
    def get_name(self):
        name_element = self._datapackage['name']

    def get_experience(self): pass

    def get_pay(self): pass

    def get_employment(self): pass

    def get_schedule(self): pass

    def get_text(self): pass

    def get_publication_data(self): pass

    def get_data(self): pass


