import json

from sqlalchemy.orm import Session

from engines import engine
from create_schema import Subprofessions, Professions, ParserElement, Service, SityNames

with open("date/professions.json") as file:
    date = json.load(file)

with Session(engine) as ses:
    def prof_data():
        for k, v in date.items():
            lis = []
            for i in v:
                s = Subprofessions(name=i)
                lis.append(s)
            d = Professions(name=k, subprofessions=lis)
            ses.add(d)
            ses.commit()


    def service_data():
        d = {"hh":"https://hh.ru/", "sj":"https://www.superjob.ru/", "rabotars":"https://www.rabota.ru/"}
        for i,n in d.items():
            n = Service(name=f"{i}")
            ses.add(n)
            ses.commit()
    def get_data_search_links():
        d = ParserElement(name_element = "link",  Xpath = """/html/body/div/div/div/div/div/div/div/main/div/div/div/div/div/div/h3/span/a/@href""", serviece  = 1)
        p = ParserElement(name_element="page_number",
                          Xpath="""/html/body/div/div/div/div/div/div/div/main/div/div/span/span/a/span html/body/div[5]/div/div[3]/div[1]/div[1]/div[3]/div[2]/main/div[5]/div/span[5]/a""",
                          serviece=1)
        p = ParserElement(name_element="page_number",
                          Xpath="""/html/body/div[5]/div/div[3]/div[1]/div[1]/div[3]/div[2]/main/div[5]/div/span[5]/a""",
                          serviece=1)
        ses.add(d)
        # ses.add(p)
        ses.commit()

    def get_data_sity():
        sity_col = ["Москва","Санкт-Петербург","Новосибирск","Екатеринбург","Казань","Нижний Новгород","Челябинск",
                    "Самара","Уфа","Ростов-на-Дону","Омск","Красноярск","Воронеж","Пермь","Волгоград"]
        for i in sity_col:
            d = SityNames(name = i)
            ses.add(d)
        ses.commit()



if __name__ == "__main__":
    # service_data()
    # prof_data()
    get_data_search_links()
    # get_data_sity()




