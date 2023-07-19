import json

from sqlalchemy.orm import Session

from engines import engine
from create_schema import Subprofessions, Professions, ParserElement, Service

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
            n = Service(name=f"{i}",link = f"{n}")
            ses.add(n)
            ses.commit()
    def get_data_search_links():
        d = ParserElement(name_element = "link", tag = "a", class_html = "serp-item__title", CSS_selector = "#a11y-main-content > div:nth-child(68) > div > div.vacancy-serp-item-body > div > div:nth-child(1) > h3 > span > a", Xpath = "/html/body/div[5]/div/div[3]/div[1]/div[1]/div[3]/div[2]/main/div[1]/div[67]/div/div[1]/div/div[1]/h3/span/a", serviece  = 1)
        k = ParserElement(name_element = "link", tag = "span", class_html = "_3mkSA _1wxkf _2tTDd K3Hxr CW-K3 _1oeJU _3330Y _17MHK", CSS_selector = "#app > div > div._1zxix > div._3C7W2 > div > div._31epc.nts52 > div._3VMkc._3JfmZ.UnlTV._3jfFx._3nFmX > div:nth-child(2) > div > div > div:nth-child(55) > div:nth-child(2) > div > div > div > div:nth-child(1) > div > div:nth-child(2) > div > div._16xI7._1pmlA > div:nth-child(1) > div > span", Xpath = """/html/body/div[3]/div/div[1]/div[5]/div/div[2]/div[1]/div[1]/div/div/div[55]/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div/span""", serviece = 2)
        n = ParserElement(name_element = "link", tag = "a", class_html = "vacancy-preview-card__title_border", CSS_selector = "#app > div.app__wrap > div.app-wrapper.app-wrapper_fixed-header.app-wrapper_mobile > div.app-wrapper__content.app-wrapper__content_fixed-header > div.app-wrapper__inner > div.layout-rabota__body > div.layout-rabota__body-inner > div > div > div.page__body > div > main > div > div:nth-child(2) > div > div > div:nth-child(1) > article > div.vacancy-preview-card__wrapper.white-box.vacancy-preview-card__wrapper_pointer > div > div.vacancy-preview-card__content-wrapper > header > h3 > a", Xpath = "/html/body/div[1]/div[2]/div/div[17]/div[2]/div[2]/div[5]/div[1]/div[2]/div/div/div[3]/div/main/div/div[2]/div/div/div[1]/article/div[2]/div/div[1]/header/h3/a", serviece = 3)
        ses.add(d)
        ses.add(k)
        ses.add(n)
        ses.commit()


if __name__ == "__main__":
    service_data()
    prof_data()
    get_data_search_links()




