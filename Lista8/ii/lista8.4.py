wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

with open("pesel.txt", 'r') as f:
    pesele = f.readlines()              # odczytanie peseli z pliku

for pesel in pesele:
    suma = 0                            # do sprawdzenia cyfry kontrolnej
    for i in range(10):
        a = int(pesel[i]) * wagi[i]     # wymnazanie kolejnych cyfr peselu przez wagi
        if a > 9:
            suma += int(str(a)[1])
        else:
            suma += a
    if str(suma)[-1] == pesel[10]:       # porownywanie ostatnie cyfry sumy z ostania z peselu
        print("Pesel jest poprawny")
        if int(pesel[9])%2 == 0:        # parzyste - kobieta
            sex = "kobieta"
        elif int(pesel[9])%2 == 1:      # nieparzyste - mezczyzna
            sex = "mężczyzna"
        print("Płeć ", sex)
        y = pesel[:2]                   # cyfry roku, miesiaca i dnia
        month = int(pesel[2:4])
        day = pesel[4:6]
        if month > 12:                  # odjecie wartosci zwiazanej z urodzeniem po 2000
            month -= 20
            year = "20" + y             # uzupelnienie
        else:
            year = "19" + y
        data = day + "." + str(month) + "." + year      # data w postaci 20.10.2020
        print("Data urodzenia: ", data)
        with open("przetworzony_pesel.txt", "a") as f:
            f.write("nr PESEL: " + pesel + "data urodzenia: " + data + ";\tpłeć: " + sex + "\n\n")
    else:
        print("Zły pesel")



