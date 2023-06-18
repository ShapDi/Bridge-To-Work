from abc import ABC,abstractmethod
import requests

class ParsingMethodAbstract(ABC):
    pass

class APIParsingMethod(ParsingMethodAbstract):
    pass

class SeleniumParsingMethod(ParsingMethodAbstract):
    pass

class RequestsParsingMethod(ParsingMethodAbstract):
    def __init__(self, url):
        self._url = url
    def receipt(self):
        response = requests.get(self._url)
        return response

class ParsingMethod():
    pass




