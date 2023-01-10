import zadanie4data

i = 1
miesiac = ""
rok = ""
dzien = ""
plec = ""
cyfraKontrolna = 0


def czyPesel(pesel, cyfraKontrolna, miesiac, rok, dzien):

    cyfraKontrolna2 = zadanie4data.kontrolna(pesel, cyfraKontrolna)   #wyznaczenie cyfry kontrolnej z pozostałych cyfr peselu

    if cyfraKontrolna2 == int(pesel[10]):         #sprawdzenie czy cyfra zgadza się tej w peselu
        miesiac = zadanie4data.miesiac(pesel, miesiac)
        dzien = zadanie4data.dzien(pesel, dzien, miesiac)
        rok = zadanie4data.rok(pesel, rok)
        if int(pesel[10]) % 2 == 0:
            plec = 'Kobieta'
        else:
            plec = 'Mezczyzna'
        if dzien != "" and dzien != None:
            tekst = "Pesel: "+pesel+" data urodzenia "+dzien+"-"+miesiac+"-"+rok+" płeć "+plec+"\n"
            prawidlowy.write(tekst)
            print("Pesel: ", pesel, end=" ")
            print("data urodzenia ", dzien, "-", miesiac, "-", rok, " płeć ", plec, sep="")

prawidlowy = open("prawidlowyPESEL.txt", 'w')
with open('PESEL.txt', 'r') as f:
    pesel = f.readline()
    if pesel != '':
        czyPesel(pesel, cyfraKontrolna, miesiac, rok, dzien)
    while pesel:
        pesel = f.readline()
        if pesel != '':
            czyPesel(pesel, cyfraKontrolna, miesiac, rok, dzien)
