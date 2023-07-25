from abc import ABC,abstractmethod
import scrapy
from bs4 import BeautifulSoup

from lxml import etree, html
import requests

cookies = {
    'hhuid': 'D3UFMNbHr7x4p2Q23WErzQ--',
    '_ym_uid': '16613442007119084',
    '_ym_d': '1681317219',
    'hhtoken': 'ioJFxBbAbKdYarDEif6CjBXdX3mF',
    'hhul': 'f0150d854cbf5eb251c9dfcf22113d8193ef91d13257f09d5a2ebaf9c3f49e97',
    '__ddg1_': 'TvGFj4p979VXP5cueyj6',
    '_xsrf': '2f744ee7c498458a0e6c54207afdadd9',
    'hhrole': 'anonymous',
    'regions': '1',
    'region_clarified': 'NOT_SET',
    'display': 'desktop',
    'crypted_hhuid': '5B47CB3AF27BBADFE2ACF40DCFA0ABD67F2875297A005862A6419C258BE20D79',
    'GMT': '3',
    'iap.uid': '32d4108af4c5485a83d683b69dcea2b8',
    '_ym_isad': '2',
    '_ga': 'GA1.2.144052942.1688426158',
    '_gid': 'GA1.2.1882173922.1688426158',
    'tmr_lvid': 'f33567d0b70c180021d37f9d59f66e35',
    'tmr_lvidTS': '1661344199791',
    '__zzatgib-w-hh': 'MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9FKnxcQ25TYHlaJ3QTCAlYIRJ8KFhXPRRcckJydS5EaB0aS2BTRVpWayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfXMoVgoOXz1EcnUxN1dhMA8WEU1HDTJoUXtMZxUTRkIce3AtLGxzVycyOSdQfyIKay8LGnxyKlILEFwvPV87Xn0wVioTSyk1IBlAZ0pINF0fQUtEIHIzd3QvQ2okYkpdH0ZaTwohC1VIM1hBEXUmCQs6Lm0tOhlRfRpdehIXQWdST0NdLSJxURR5DiplMy1sImd7WVJ2Vwk0LR8Yd20qVgg8XEREKy0uPmYjYXlbVDVRP0FaW1Q4NmdBEXUmCQg3LGBwVxlRExpceEdXeishFn5uJlN/DmBAQWllbQwtUlFRS2IPHxo0aQteTA==6nuYaw==',
    'device_magritte_breakpoint': 's',
    'device_breakpoint': 'xs',
    'total_searches': '3',
    '_gat_gtag_UA_11659974_2_DG': '1',
    'tmr_detect': '0%7C1688497867543',
    'cfidsgib-w-hh': 'atiB4C1i2p5Dn8UyhZ9sVsAI/B2XRASdCpTP+pYmrAvvbgMh7iw+Jw3+JeSzwqWndTewgi3AC6VZz9moNAY9Oi241ItxEY/ZD+n+ugxL/D2erpl+YVie4Y5cqNbta4hyL93p8hilqlDUnVWOXSjM3d189ViMYSe+EhrCSr7gtQ==',
    'cfidsgib-w-hh': 'atiB4C1i2p5Dn8UyhZ9sVsAI/B2XRASdCpTP+pYmrAvvbgMh7iw+Jw3+JeSzwqWndTewgi3AC6VZz9moNAY9Oi241ItxEY/ZD+n+ugxL/D2erpl+YVie4Y5cqNbta4hyL93p8hilqlDUnVWOXSjM3d189ViMYSe+EhrCSr7gtQ==',
    'gsscgib-w-hh': 'AuF1DZhTaNJmdlITj/SC9zAioU8hdnx8jyHHdJCd6getSqrY7OXrGvNvFEns4hGfkLBANPxSfu84bagUgUF0vDhKWwUUdyReWP+M+5o2119qRY+PK/pndJNlmnHWvAz3yzLA7ug0yCdIeTICKloQ3tJr7/SBUrYx9GifdIUzo6hTm5PeOqw1lqb9KF499B56ebPpndT4mRlobY0pl6hGtxxIqfyegT203/6/RV9ySfwgUKVeRgL6YMwtaKgIFA==',
    'fgsscgib-w-hh': 'P63c08712e69d73b4217a7ba72cf20dd8403a739',
}

headers = {
    'authority': 'hh.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'hhuid=D3UFMNbHr7x4p2Q23WErzQ--; _ym_uid=16613442007119084; _ym_d=1681317219; hhtoken=ioJFxBbAbKdYarDEif6CjBXdX3mF; hhul=f0150d854cbf5eb251c9dfcf22113d8193ef91d13257f09d5a2ebaf9c3f49e97; __ddg1_=TvGFj4p979VXP5cueyj6; _xsrf=2f744ee7c498458a0e6c54207afdadd9; hhrole=anonymous; regions=1; region_clarified=NOT_SET; display=desktop; crypted_hhuid=5B47CB3AF27BBADFE2ACF40DCFA0ABD67F2875297A005862A6419C258BE20D79; GMT=3; iap.uid=32d4108af4c5485a83d683b69dcea2b8; _ym_isad=2; _ga=GA1.2.144052942.1688426158; _gid=GA1.2.1882173922.1688426158; tmr_lvid=f33567d0b70c180021d37f9d59f66e35; tmr_lvidTS=1661344199791; __zzatgib-w-hh=MDA0dC0pXB4IH04NIH5rL2R7RSRfHDx1ZS9FKnxcQ25TYHlaJ3QTCAlYIRJ8KFhXPRRcckJydS5EaB0aS2BTRVpWayELUTQ1ZhBKT01HMzg/aH0eVBw5VREPFhI2FyMSfXMoVgoOXz1EcnUxN1dhMA8WEU1HDTJoUXtMZxUTRkIce3AtLGxzVycyOSdQfyIKay8LGnxyKlILEFwvPV87Xn0wVioTSyk1IBlAZ0pINF0fQUtEIHIzd3QvQ2okYkpdH0ZaTwohC1VIM1hBEXUmCQs6Lm0tOhlRfRpdehIXQWdST0NdLSJxURR5DiplMy1sImd7WVJ2Vwk0LR8Yd20qVgg8XEREKy0uPmYjYXlbVDVRP0FaW1Q4NmdBEXUmCQg3LGBwVxlRExpceEdXeishFn5uJlN/DmBAQWllbQwtUlFRS2IPHxo0aQteTA==6nuYaw==; device_magritte_breakpoint=s; device_breakpoint=xs; total_searches=3; _gat_gtag_UA_11659974_2_DG=1; tmr_detect=0%7C1688497867543; cfidsgib-w-hh=atiB4C1i2p5Dn8UyhZ9sVsAI/B2XRASdCpTP+pYmrAvvbgMh7iw+Jw3+JeSzwqWndTewgi3AC6VZz9moNAY9Oi241ItxEY/ZD+n+ugxL/D2erpl+YVie4Y5cqNbta4hyL93p8hilqlDUnVWOXSjM3d189ViMYSe+EhrCSr7gtQ==; cfidsgib-w-hh=atiB4C1i2p5Dn8UyhZ9sVsAI/B2XRASdCpTP+pYmrAvvbgMh7iw+Jw3+JeSzwqWndTewgi3AC6VZz9moNAY9Oi241ItxEY/ZD+n+ugxL/D2erpl+YVie4Y5cqNbta4hyL93p8hilqlDUnVWOXSjM3d189ViMYSe+EhrCSr7gtQ==; gsscgib-w-hh=AuF1DZhTaNJmdlITj/SC9zAioU8hdnx8jyHHdJCd6getSqrY7OXrGvNvFEns4hGfkLBANPxSfu84bagUgUF0vDhKWwUUdyReWP+M+5o2119qRY+PK/pndJNlmnHWvAz3yzLA7ug0yCdIeTICKloQ3tJr7/SBUrYx9GifdIUzo6hTm5PeOqw1lqb9KF499B56ebPpndT4mRlobY0pl6hGtxxIqfyegT203/6/RV9ySfwgUKVeRgL6YMwtaKgIFA==; fgsscgib-w-hh=P63c08712e69d73b4217a7ba72cf20dd8403a739',
    'pragma': 'no-cache',
    'referer': 'https://hh.ru/search/vacancy?text=python',
    'sec-ch-ua': '"Opera GX";v="99", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0',
}




class APIParsingMethod():
    pass

class SeleniumParsingMethod():
    pass
class RequestsParsingMethod():

    def __init__(self, url:str, elements:list):
        self._url = url
        self._elements = elements


    def get_element(self):
        page = requests.get(self._url, cookies=cookies, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        dom = etree.HTML(str(soup))
        list_element = []
        for i in self._elements:
            try:
                list_element.append(list(map(lambda i: i.text, (dom.xpath(i)))))
            except:
                list_element.append(dom.xpath(i))
        return list_element[0]







