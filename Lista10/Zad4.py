#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup
import requests


def get_html(url: str, path: str) -> str:
    response = requests.get(url)
    open(path, 'w').write(response.text)


def main():
    os.system('clear')
    url = 'https://www.nbp.pl/kursy/xml/a012z230118.xml'
    path = 'Lista10/kursy.xml'
    get_html(url, path)

if __name__ == '__main__':
    main()
