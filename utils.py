import datetime as DT
import requests
from decimal import Decimal
from bs4 import BeautifulSoup



def currency_rates_adv(code: str) -> (Decimal, DT.date):
    """возвращает курс валюты `code` по отношению к рублю"""

    cbr_url = "http://www.cbr.ru/scripts/XML_daily.asp"
    req = requests.get(cbr_url)
    soup = BeautifulSoup(req.text, 'lxml')
    day_value = DT.datetime.strptime(soup.find("valcurs")['date'],'%d.%m.%Y')
    for tag in soup.findAll("valute"):
        char_code = tag.find('charcode').text
        value = Decimal(tag.find('value').text.replace(',', '.')) / Decimal(tag.find('nominal').text.replace(',', '.'))
        if code.lower() == char_code.lower():
            return value, day_value.date()
    return None, None


"""
if __name__ == "__main__":
    kurs, date_value = currency_rates_adv("USD")

    empty = bool(not kurs and not date_value)
    if empty or not isinstance(kurs, Decimal):
        raise TypeError("Неверный тип данных у курса")
    if empty or not isinstance(date_value, DT.date):
        raise TypeError("Неверный тип данных у даты")
    print(kurs, date_value)
"""

