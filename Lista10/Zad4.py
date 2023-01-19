#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup
import requests
from dotenv import dotenv_values
from datetime import date, timedelta


class Currency:
    url = 'https://www.nbp.pl/kursy/xml/a012z230118.xml'

    def __init__(self, path: str):
        self.path = path
        self.file = BeautifulSoup(open(path), 'xml')
        Currency.get_html(self, self.url)

    def get_html(self, url: str):
        if not os.path.isfile(self.path) or self.file.find('data_publikacji').text != (date.today() - timedelta(days=1)).strftime('%Y-%m-%d'):
            response = requests.get(url)
            open(self.path, 'w').write(response.text)

    def get_currency(self, code: str):
        code_parent = self.file.find('kod_waluty', text=code).parent
        exchange_rate = float(code_parent.find('kurs_sredni').text.replace(',', '.'))
        return exchange_rate

    def calculate_pln(self, code: str, amount: float):
        exchange_rate = Currency.get_currency(self, code)
        return f'{amount} {code} = {amount * exchange_rate} PLN'

    def calculate_curr_curr(self, code_1: str, code_2: str, amount: float):
        currency_1 = Currency.get_currency(self, code_1)
        currency_2 = Currency.get_currency(self, code_2)
        return f'{amount} {code_1} = {round((amount * currency_1 / currency_2), 3)} {code_2}'




def main():
    os.system('clear')
    path = dotenv_values()['PATH']
    currency = Currency(path)
    print(currency.calculate_pln('THB', 100))
    print(currency.calculate_curr_curr('USD', 'THB', 100))


if __name__ == '__main__':
    main()
