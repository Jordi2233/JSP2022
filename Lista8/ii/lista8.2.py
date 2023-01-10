import SzyfrCezara
import datetime
import os
import glob
path = input("Podaj ścieżkę do plikow: ")
# path = "test"
if not os.path.exists(path):
    print("Nie ma takiej ścieżki")
else:
    pliki = glob.glob(path + "/*.txt")       # lista plikow txt
    for plik in pliki:
        przesun = plik[-14]                  # { nr_data.txt } -> 14 znakow
        try:
            print(plik)
            with open(plik, 'r') as f:
                text = f.readlines()
                print(text)
            try:
                newfile = path + "/plik_deszyfrowany_" + plik[-14:]
                with open(newfile, 'w+') as f:
                    for i in range(len(text)):
                        text[i] = SzyfrCezara.deszyfr(text[i], int(przesun))
                    print(text)
                    f.writelines(text)
            except IOError:
                print("Nie udało się poprawnie deszyfrować pliku i zapisać w danej ścieżce")
        except IOError:
            print("Nie udało się odczytac pliku")


