import logging

from models.data_recording import DataRecording
from models.typical_requests import get_data_package, get_data_profession
from core.aggregator import Aggregator

class Controller():
    set_aggregators = []

    def __init__(self, dataprofession:dict, datapackage:dict,session:bool):
        self._dataprofession = dataprofession
        self._datapackage = datapackage
        self._session = session

    def initialization_aggregator(self):
        for profession,subprofesson in self._dataprofession.items():
            self.set_aggregators.append(Aggregator(profession,subprofesson,self._datapackage))
        for i in self.set_aggregators:
            i.initialization_agregators()

    def aggregator_link(self):
        for i in self.set_aggregators:
            for n in i.get_links():
                with open("new.txt","w") as file:
                    file.write(str(n))
                DataRecording(n).saving_link()

    def aggregator_vacancies(self):
        pass

    def removal_aggregator(self):
        pass


def start_controller():
    core_comtroller = Controller(get_data_profession(),get_data_package(), session=True)
    core_comtroller.initialization_aggregator()
    core_comtroller.aggregator_link()


if __name__ == "__main__":
    start_controller()


