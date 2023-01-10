import SzyfrCezara
import datetime
import os
p = int(input("Podaj przesunięcie [1-10]: "))
file = input("Podaj ścieżkę do pliku i jego nazwe: ")      # pycharm wzgledem aktualnej pozycji - folderu
# file = "plik_do_szyfrowania.txt"
path = input("Podaj ścieżkę do zapisu: ")
# path = "test"

try:                                            # sprobuj stworzyc sciezke
    os.makedirs(path)
except OSError:
    print("Nie udało się stworzyć danej ścieżki lub takowa istnieje (jeśli istnieje to tam spróbujemy zapisać plik)")

try:                                            # sprobuj:
    with open(file, 'r') as f:                  # otworzyc i odczytac (do zmienej)
        text = f.readlines()
        print(text)
    try:                                        # sprobuj(2) rozszyfrowac
        curr_time = datetime.datetime.now()
        year = str(curr_time.year)

        if curr_time.month < 10:
            month = "0" + str(curr_time.month)
        if curr_time.day < 10:
            day = "0" + str(curr_time.day)

        newfile = path + "/plik_zaszyfrowany_" + str(p) + "_" + year + month + day + ".txt"
        with open(newfile, 'w+') as f:
            for i in range(len(text)):
                text[i] = SzyfrCezara.szyfr(text[i], p)
            print(text)
            f.writelines(text)
    except IOError:
        print("Nie udało się poprawnie zaszyfrować pliku i zapisać w danej ścieżce")
except IOError:
    print("Nie udało się odczytac pliku")



