from dataclasses import dataclass
@dataclass
class DataParsingElements:
    name:str
    experience:str
    pay:str
    employment:str
    schedule:str
    text:str
    publication:str
    city:str

@dataclass
class DataServiceVacancy():
    hh:DataParsingElements
    sj:DataParsingElements
    rr:DataParsingElements


@dataclass
class DataServicelink():
    hh:str
    sj:str
    rr:str

