import re
import spacy

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime

class DetailsExtractor:
    def __init__(self, string):
        self.string = string
        self.promo_code, self.text = self.extract_promo_code()

    def nlp_parser(self):
        nlp = spacy.load("en_core_web_md")
        doc = nlp(self.text)
        return doc
    
    def extract(self):
        data = {
            "date": self.extract_date(),
            "name": self.extract_name(),
            "destination": self.extract_destination(),
            "promo_code": self.promo_code,
        }
        return data

    def extract_promo_code(self):
        promo_code = re.findall(r"\[(.*?)\]", self.string)[0]
        text = re.findall(r"\](.*)", self.string)[0].strip()
        return promo_code, text
    
    def extract_name(self):
        doc = self.nlp_parser()
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text
        return None
    
    def extract_destination(self):
        doc = self.nlp_parser()
        for ent in doc.ents:
            if ent.label_ == "GPE":
                return ent.text
        return None

    def extract_date(self):
        doc = self.nlp_parser()
        for ent in doc.ents:
            if ent.label_ == "DATE":
                return self.parse_date(ent.text).strftime("%Y-%m-%d")
        return None
    
    def parse_date(self, dateStr):
        weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

        while not any(char.isdigit() for char in dateStr.split(" ")[0]) and dateStr.split(" ")[0].lower() not in weekdays and dateStr.split(" ")[0].lower() not in months:
            dateStr = dateStr.split(" ", 1)[1]
            if len(dateStr.split(" ")) == 1:
                break

        tempDateStr = dateStr
        # check if tempDateStr contains th, st, nd, rd
        if any(suffix in tempDateStr for suffix in ["th", "st", "nd", "rd"]):
            if parse(dateStr, default=datetime(datetime.today().year, datetime.today().month, datetime.today().day)).date() > datetime.today().date():
                return(parse(dateStr, default=datetime(datetime.today().year, datetime.today().month, datetime.today().day)).date())
            else:
                return(parse(dateStr, default=datetime(datetime.today().year, datetime.today().month, datetime.today().day)).date() + relativedelta(years=1))
        else:
            weekday_index = weekdays.index(tempDateStr) if tempDateStr in weekdays else None
            month_index = months.index(tempDateStr) if tempDateStr in months else None

            # Calculate the date based on the index
            if weekday_index is not None:
                date = datetime.now().date() + relativedelta(weekday=weekday_index)
                return(date)
            elif month_index is not None:
                date = datetime.now().date() + relativedelta(months=month_index)
                return(date)
            elif any(char.isdigit() for char in tempDateStr):
                for i in range(len(tempDateStr)):
                    if tempDateStr[i].isdigit():
                        if tempDateStr[i+1].isdigit():
                            if tempDateStr[i+2].isdigit():
                                return(parse(tempDateStr[i:i+3], default=datetime(datetime.today().year, datetime.today().month, datetime.today().day)).date())
                                break
                            else: 
                                return(parse(tempDateStr[i:i+2], default=datetime(datetime.today().year, datetime.today().month, datetime.today().day)).date())
                                break
                        else:
                            return(parse(tempDateStr[i], default=datetime(datetime.today().year, datetime.today().month, datetime.today().day)).date())
                            break