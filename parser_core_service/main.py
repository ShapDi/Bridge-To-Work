from models.typical_requests import get_data_package
from core.collectors import Aggregator
class Controller():
    DATAPACKAGE = get_data_package()
    set_aggregators = []
    @staticmethod
    def initialization_aggregator(profession:str,subprofession:list):
        new_aggregator = Aggregator(profession = profession,subprofession = subprofession)
        Controller.set_aggregators.append(new_aggregator)

    @staticmethod
    def start_aggregator(aggregator = set_aggregators):
        if type(aggregator) == list:
            for i in aggregator:
                i.get_links
        else:
            aggregator.get_links

    @staticmethod
    def removal_aggregator():
        pass
    @classmethod
    def god(element, comand:str):
        pass





def main():
    pass


print("initialization")

