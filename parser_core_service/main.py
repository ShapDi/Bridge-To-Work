from models.typical_requests import get_data_package, get_data_profession
from core.collectors import Aggregator



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

    def start_aggregator(self):
        for i in self.set_aggregators:
            d = i.get_links()
            with open("file.txt","w") as file:
                file.write(d)



    def removal_aggregator(self):
        pass


def main():
    # get_data_profession(),
    core_comtroller = Controller(get_data_profession(),get_data_package(), session=True)
    core_comtroller.initialization_aggregator()
    core_comtroller.start_aggregator()




if __name__ == "__main__":
    main()


