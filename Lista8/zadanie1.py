import cezar
import time
import os.path
from datetime import date

today = date.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)

key = 11
while (key > 10) or (key < 1):
    key = int(input("Podaj przesunięcie szyfru (od 1 do 10) "))

strKey = str(key)
name = input("Podaj nazwe pliku do zaszyfrowania (np. 'plik_do_szyfrowania') ");
name = name + ".txt"
path = input("Podaj ścieżkę zapisu pliku (np. 'zaszyfrowane') ");

namefile = "plik_zaszyfrowany" + strKey + '_' + str(today.year) + str(today.month) + str(today.day) + ".txt"
try:
    new = open(os.path.join(path,namefile),"w+") #write/read + create file if not exist
    try:
        with open(name, 'r') as f: #'r' - read
            print('plik istnieje!')
            print('szyfrowanie...')
            zaszyfrowany = cezar.szyfrowanie(f.read(), key)
            new.write(zaszyfrowany)
            print(zaszyfrowany)
    except IOError:
        print("Nie znaleziono pliku", name, "!")
except IOError:
    print("Nie znaleziono takiego katalogu do wczytania pliku!")
