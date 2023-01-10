import cezar
import time
import os.path
from datetime import date

today = date.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)
directory = input("Podaj katalog do odczytu(np. 'zaszyfrowane') ")
directory = r''+directory+'/'
try:
    for file in os.listdir(directory):
        try:
            if file.endswith(".txt"):
                name = directory+file
                key = int(file[17])
                new = 'plik_deszyfrowany' + str(key) + '_' + str(today.year) + str(today.month) + str(today.day) + ".txt"
                try:
                    with open(name, 'r') as szyfr:
                        deszyfr = szyfr.read()
                        deszyfr = cezar.deszyfrowanie(deszyfr, key)
                        odszyfrowane = open(os.path.join('odszyfrowane/', new), "w+")  # write + create if not exist
                        odszyfrowane.write(deszyfr)
                        print("plik ", file, " został odszyfrowany!")
                    odszyfrowane.close()
                except IOError:
                    print("Wystąpił problem podczas otwierania pliku", name)
            else:
                continue
        except IOError:
            print("Nie można otworzyć pliku ", file, "do odczytu")
except IOError:
    print("Nie znaleziono katalogu ", directory, " do odczytu")
