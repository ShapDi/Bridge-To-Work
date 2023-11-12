from abc import ABC, abstractmethod

from .parsing_methods import RequestsParsingMethod


class LinkCleaner:
    def __init__(self, text):
        self._text = text

    def сlearing_link(self):
        link = self._text.split('?')[0]
        return link


class Auditor:
    def __init__(self, audit_object, element):
        self._audit_object = audit_object
        self._element = element

    def check_presence(self):
        number_element = self._audit_object.find(self._element)
        if number_element == -1:
            result = False
        else:
            result = True
        return result


class InformationAggregatorAbstract(ABC):
    def get_name(self):
        return self._datapackage.name
    def get_experience(self):
        return self._datapackage.experience
    def get_pay(self):
        return self._datapackage.pay
    def get_city(self):
        return self._datapackage.city
    def get_time_job(self):
        return self._datapackage.time_job
    def get_schedule(self):
        return self._datapackage.schedule
    def get_text(self):
        return self._datapackage.text
    def get_publication_date(self):
        return self._datapackage.publication_date
    def get_education(self):
        return self._datapackage.education

    @abstractmethod
    def get_data(self): pass

class InformationAggregatorHH(InformationAggregatorAbstract):
    def __init__(self, link, datapackage):
        self._link = link
        self._datapackage = datapackage

    # def get_name(self):
    #     return self._datapackage['name']
    #
    # def get_experience(self):
    #     return self._datapackage['experience']
    #
    # def get_schedule(self):
    #     return self._datapackage['schedule']
    #
    # def get_text(self):
    #     return self._datapackage['text']
    #
    # def get_publication_data(self):
    #     return self._datapackage['text']
    #
    # def get_city(self): pass

    def get_data(self):
        print(self._datapackage)
        return RequestsParsingMethod(self._link).get_elements(elements = {'name':self.get_name(),
                                                               'experience':self.get_experience(),
                                                               'pay':self.get_pay(),
                                                               'city':self.get_city(),
                                                               'time_job':self.get_time_job(),
                                                               'schedule':self.get_schedule(),
                                                               'text':self.get_text(),
                                                               'publication_date':self.get_publication_date(),
                                                               'education':self.get_education()})

class InformationAggregatorSJ(InformationAggregatorAbstract):
    def __init__(self, datapackage):
        self._datapackage = datapackage

    def get_data(self):
        pass


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
