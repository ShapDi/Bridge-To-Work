import redis

from models.add_methods import add_link
from models.get_methods import get_job_search_data, get_data_sity
from core import ControllerVacancies, ControllerLinks
from core import DataParsingElements, DataServiceVacancy, DataServicelink
from models.get_methods import get_links_rr, get_links_sj, get_links_hh
from models.get_methods import get_data_profession








data = get_job_search_data()
print(data)

hh_data = data['hh']
hh_data = DataParsingElements(name = hh_data['name'].get('Xpath'),
                              experience = hh_data['experience'].get('Xpath'),
                              education = hh_data['education'].get('Xpath'),
                              time_job = hh_data['time_job'].get('Xpath'),
                              pay = hh_data['pay'].get('Xpath'),
                              city = hh_data['city'].get('Xpath'),
                              schedule = hh_data['schedule'].get('Xpath'),
                              text = hh_data['text'].get('Xpath'),
                              publication_date = hh_data['publication_date'].get('Xpath'))
sj_data = data['sj']
sj_data = DataParsingElements(name = sj_data['name'].get('Xpath'),
                              experience = sj_data['experience'].get('Xpath'),
                              education = sj_data['education'].get('Xpath'),
                              time_job = sj_data['time_job'].get('Xpath'),
                              pay = sj_data['pay'].get('Xpath'),
                              city = sj_data['city'].get('Xpath'),
                              schedule = sj_data['schedule'].get('Xpath'),
                              text = sj_data['text'].get('Xpath'),
                              publication_date = sj_data['publication_date'].get('Xpath'))
rr_data = data['rr']
rr_data = DataParsingElements(name = rr_data['name'].get('Xpath'),
                              experience = rr_data['experience'].get('Xpath'),
                              time_job = rr_data['time_job'].get('Xpath'),
                              education = rr_data['education'].get('Xpath'),
                              pay = rr_data['pay'].get('Xpath'),
                              city = rr_data['city'].get('Xpath'),
                              schedule = rr_data['schedule'].get('Xpath'),
                              text = rr_data['text'].get('Xpath'),
                              publication_date = rr_data['publication_date'].get('Xpath'))
# link_data = data['hh'].get('link').get('Xpath')
# link_data = data['sj'].get('link').get('Xpath')
# link_data = data['rr'].get('link').get('Xpath')

# data_package_link = DataServicelink(hh = data['hh'].get('link').get('Xpath'), sj = data['sj'].get('link').get('Xpath'), rr = data['rr'].get('link').get('Xpath'))

data_package = DataServiceVacancy(hh = hh_data, sj = sj_data, rr = rr_data)



# base_controller_link = ControllerLinks(name = 'base_controller', data_package = data_package_link)
# for sity in get_data_sity():
#     for hh in get_data_profession():
#         for link in base_controller_link.get_job_data_link(service = 'hh', request = hh.name + ' ' + sity.name):
#             add_link(link = link,sity = sity.id , subprofessions = hh.id ,service_id = 1)

base_controller_vacancies = ControllerVacancies(name = 'base_controller', data_package = data_package)

def get_vacant():
    for hh_link in get_links_hh():
        print(hh_link)
        yield ['hh',base_controller_vacancies.get_job_data_collection(service = 'hh', link = hh_link.link)]
    # for sj_link in get_links_sj():
    #     yield ['sj',base_controller_vacancies.get_job_data_collection(service = 'sj', link = sj_link.link)]
    # for rr_link in get_links_rr():
    #     yield ['rr',base_controller_vacancies.get_job_data_collection(service = 'rr', link = rr_link.link)]
    #


for i in get_vacant():
    print(i)