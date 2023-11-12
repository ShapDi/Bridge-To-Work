from dataclasses import dataclass
@dataclass
class DataParsingElements:
    name:str
    experience:str
    pay:str
    time_job:str
    schedule:str
    text:str
    publication_date:str
    education:str
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

