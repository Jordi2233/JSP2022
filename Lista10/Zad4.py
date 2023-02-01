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
        self.get_html(self.url)

    def get_html(self, url: str):
        if not os.path.isfile(self.path) or self.file.find('data_publikacji').text != (date.today() - timedelta(days=1)).strftime('%Y-%m-%d'):
            response = requests.get(url)
            open(self.path, 'w').write(response.text)

    def get_currency(self, code: str):
        code_parent = self.file.find('kod_waluty', text=code).parent
        exchange_rate = float(code_parent.find(
            'kurs_sredni').text.replace(',', '.'))
        return exchange_rate

    def calculate_pln_currency(self, code: str, amount: float):
        exchange_rate = self.get_currency(code)
        pln_to_currency = f'{amount} PLN <-> {amount / exchange_rate:.2f} {code}'
        currency_to_pln = f'{amount} {code} = {amount * exchange_rate} PLN'
        return pln_to_currency, currency_to_pln

    def f_curr_to_sec_curr(self, code_1: str, code_2: str, amount: float):
        currency_1 = self.get_currency(code_1)
        currency_2 = self.get_currency(code_2)
        return f'{amount} {code_1} <-> {amount * currency_1 / currency_2:.2f} {code_2}'


def main():
    os.system('clear')
    path = dotenv_values()['PATH']
    currency = Currency(path)
    print("What do you want to do?")
    print("1) PLN <-> Currency")
    print("2) Currency <-> PLN")
    print("3) Currency1 <-> Currency2")
    print("4) Exit")
    mod = input("Your choice: ")

    try:
        match mod:

            case '1':
                code = input("Currency code: ")
                value = float(input("Value: "))
                print(currency.calculate_pln_currency(code, value)[0])

            case '2':
                value = float(input("Value: "))
                code = input("Currency code: ")
                print(currency.calculate_pln_currency(code, value)[1])

            case '3':
                code_1 = input("First currency code: ")
                code_2 = input("Second currency code: ")
                value = float(input("Value: "))
                print(currency.f_curr_to_sec_curr(code_1, code_2, value))

            case '4':
                exit()
    except AttributeError:
        print("Wrong currency code!")


if __name__ == '__main__':
    main()
