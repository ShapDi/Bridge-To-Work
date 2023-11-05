from core import ControllerVacancies, ControllerLinks
from core import DataParsingElements,DataServiceVacancy
from models.get_methods import get_links_rr, get_links_sj, get_links_hh


def get_vacant():
    for hh in get_links_hh:
        return ControllerVacancies()
    for sj in get_links_sj:
        return ControllerVacancies()
    for rr in get_links_rr:
        return ControllerVacancies()