import logging

from models.data_recording import DataRecording
from models.get_methods import get_data_package, get_data_profession

from core.accumulation_vacancies import InformationAggregatorHH, InformationAggregatorRR, InformationAggregatorSJ
from core.accumulation_links import LinkCollectionAggregatorHH, LinkCollectionAggregatorRR, LinkCollectionAggregatorSJ
class ControllerLinks:

    SERVICE_STRATEGIES = {"hh": LinkCollectionAggregatorHH,
                          "sj": LinkCollectionAggregatorRR,
                          "rb": LinkCollectionAggregatorSJ}
    def __init__(self, name, data_package):
        self._name = name
        self._data_package = data_package


    def get_job_data_link(self, service, request):
        return self.SERVICE_STRATEGIES[service](request, self._data_package).getting_links()


class ControllerVacancies:
    SERVICE_STRATEGIES = {"hh": InformationAggregatorHH,
                          "sj": InformationAggregatorSJ,
                          "rb": InformationAggregatorRR}

    def __init__(self, name, data_package):
        self._name = name
        self._data_package = data_package

    def get_job_data_collection(self, service: str, link: str):
        return self.SERVICE_STRATEGIES[service](link = link, datapackage = self._data_package.hh).get_data()

    def __str__(self):
        return self._name


