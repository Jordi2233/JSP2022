#!/usr/bin/env python3
import os

from datetime import date


class Obywatel:
    def __init__(self, name, nazwisko, data_urodzenia):
        if data_urodzenia > date.today():
            raise ValueError("Data urodzenia nie może być w przyszłości")
        self.fName = name
        self.lName = nazwisko
        self.born_date = data_urodzenia
        self.age = (date.today() - self.born_date).days // 365

    def __str__(self):
        return f"Obywatel/ka {self.fName} {self.lName}, {self.age} lat, urodzony {self.born_date}."


def main():
    os.system('clear')

    osob = Obywatel("Jan", "Kowalski", date(2002, 3, 2))
    print(osob)


if __name__ == '__main__':
    main()
