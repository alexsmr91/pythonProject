import requests
from decimal import Decimal
from bs4 import BeautifulSoup



def currency_rates(code: str) -> Decimal:
    """возвращает курс валюты `code` по отношению к рублю"""

    cbr_url = "http://www.cbr.ru/scripts/XML_daily.asp"
    req = requests.get(cbr_url)
    soup = BeautifulSoup(req.text, 'lxml')

    for tag in soup.findAll("valute"):
        char_code = tag.find('charcode').text
        value = Decimal(tag.find('value').text.replace(',', '.')) / Decimal(tag.find('nominal').text.replace(',', '.'))
        if code.lower() == char_code.lower():
            return value



print(currency_rates("USD"))
print(currency_rates("AMD"))
print(currency_rates("noname"))