
@dataclass
class DataServiceVacancy():
    hh:DataParsingElements
    superjob:DataParsingElements
    rabota_ru:DataParsingElements
@dataclass
class DataParsingElements():
    name:str
    experience:str
    pay:str
    employment:str
    schedule:str
    text:str
    publication:str
    city:str




