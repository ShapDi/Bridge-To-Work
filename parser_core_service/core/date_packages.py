from pydantic import BaseModel


class DataServiceСollection(BaseModel):
    hh:dict
    superjob:dict
    rabota_ru:dict


class DataServiceLink(BaseModel):
    xpath:dict
    sity: dict


class DataServiceVacancy(BaseModel):
    link:str
    xpath:dict
    sity: str


