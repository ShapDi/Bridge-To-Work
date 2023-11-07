import redis

from models.add_methods import add_link
from models.get_methods import get_job_search_data, get_data_sity
from core import ControllerVacancies, ControllerLinks
from core import DataParsingElements, DataServiceVacancy, DataServicelink
from models.get_methods import get_links_rr, get_links_sj, get_links_hh
from models.get_methods import get_data_profession








data = get_job_search_data()

hh_data = data['hh']
hh_data = DataParsingElements(name = hh_data['name'].get('Xpath'),
                              experience = hh_data['experience'].get('Xpath'),
                              employment = hh_data['education'].get('Xpath'),
                              pay = hh_data['pay'].get('Xpath'),
                              city = hh_data['city'].get('Xpath'),
                              schedule = hh_data['schedule'].get('Xpath'),
                              text = hh_data['text'].get('Xpath'),
                              publication = hh_data['publication_date'].get('Xpath'))
sj_data = data['sj']
sj_data = DataParsingElements(name = sj_data['name'].get('Xpath'),
                              experience = sj_data['experience'].get('Xpath'),
                              employment = sj_data['education'].get('Xpath'),
                              pay = sj_data['pay'].get('Xpath'),
                              city = sj_data['city'].get('Xpath'),
                              schedule = sj_data['schedule'].get('Xpath'),
                              text = sj_data['text'].get('Xpath'),
                              publication = sj_data['publication_date'].get('Xpath'))
rr_data = data['rr']
rr_data = DataParsingElements(name = rr_data['name'].get('Xpath'),
                              experience = rr_data['experience'].get('Xpath'),
                              employment = rr_data['education'].get('Xpath'),
                              pay = rr_data['pay'].get('Xpath'),
                              city = rr_data['city'].get('Xpath'),
                              schedule = rr_data['schedule'].get('Xpath'),
                              text = rr_data['text'].get('Xpath'),
                              publication = rr_data['publication_date'].get('Xpath'))
# link_data = data['hh'].get('link').get('Xpath')
# link_data = data['sj'].get('link').get('Xpath')
# link_data = data['rr'].get('link').get('Xpath')

data_package_link = DataServicelink(hh = data['hh'].get('link').get('Xpath'), sj = data['sj'].get('link').get('Xpath'), rr = data['rr'].get('link').get('Xpath'))

data_package = DataServiceVacancy(hh = hh_data, sj = sj_data, rr = rr_data)



base_controller_link = ControllerLinks(name = 'base_controller', data_package = data_package_link)
for sity in get_data_sity():
    for hh in get_data_profession():
        for link in base_controller_link.get_job_data_link(service = 'hh', request = hh.name + ' ' + sity.name):
            add_link(link = link,sity = sity.id , subprofessions = hh.id ,service_id = 1)

base_controller_vacancies = ControllerVacancies(name = 'base_controller', data_package = data_package)

def get_vacant():
    for hh_link in get_links_hh():
        return base_controller_vacancies.get_job_data_collection(service = 'hh', link = hh_link)
    for sj_link in get_links_sj():
        return base_controller_vacancies.get_job_data_collection(service = 'sj', link = sj_link)
    for rr_link in get_links_rr():
        return base_controller_vacancies.get_job_data_collection(service = 'rr', link = rr_link)