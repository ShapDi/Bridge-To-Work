import logging

from models.data_recording import DataRecording
from models.get_methods import get_data_package, get_data_profession
from core.aggregator import Aggregator
from core.accumulation_vacancies import InformationAggregatorHH, InformationAggregatorRR, InformationAggregatorSJ


# from core.date_packages import DataParsingElements

class ControllerLinks():
    set_aggregators = []

    def __init__(self, dataprofession: dict, datapackage: dict, session: bool):
        self._dataprofession = dataprofession
        self._datapackage = datapackage
        self._session = session

    def initialization_aggregator(self):
        for profession, subprofesson in self._dataprofession.items():
            self.set_aggregators.append(Aggregator(profession, subprofesson, self._datapackage))
        for i in self.set_aggregators:
            i.initialization_agregators()

    def aggregator_link(self):
        for i in self.set_aggregators:
            for n in i.get_links():
                with open("new.txt", "w") as file:
                    file.write(str(n))
                DataRecording(n).saving_link()


class Packer:
    def __init__(self, data):
        self._data = data


class ControllerVacancies:
    SERVICE_STRATEGIES = {"hh": InformationAggregatorHH,
                          "sj": InformationAggregatorSJ,
                          "rb": InformationAggregatorRR}

    def __init__(self, name, data_package):
        self._name = name
        self._data_package = data_package

    def get_job_data_collection(self, service: str, link: str):
        return self.SERVICE_STRATEGIES[service](self._data_package, link)

    def __str__(self):
        return self._name


def start_controller_links():
    core_controller = ControllerLinks(get_data_profession(), get_data_package(), session = True)
    core_controller.initialization_aggregator()
    core_controller.aggregator_link()


# def start_controller_vacancies():
#     ControllerVacancies(links = get_link_registration())


if __name__ == "__main__":
    start_controller_links()
