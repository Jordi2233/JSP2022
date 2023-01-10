import random

rokUrodzenia = str(random.randrange(1800, 2299))

rok = rokUrodzenia[2] + rokUrodzenia[3]

miesiac = ""
miesiacUrodzenia = str(random.randrange(1, 12))
if len(miesiacUrodzenia) == 1:
    miesiacUrodzenia = '0' + miesiacUrodzenia

plec = str(random.randrange(1000, 9999))

if int(miesiacUrodzenia) == 1 or int(miesiacUrodzenia) == 3 or int(miesiacUrodzenia) == 5 or int(
        miesiacUrodzenia) == 7 or int(miesiacUrodzenia) == 8 or int(miesiacUrodzenia) == 10 or int(
        miesiacUrodzenia) == 12:
    dzien = str(random.randrange(1, 31))
else:
    if int(miesiacUrodzenia) != 2:
        dzien = str(random.randrange(1, 30))
    else:
        if int(rokUrodzenia[3]) % 2 == 0:
            dzien = str(random.randrange(1, 29))
        else:
            dzien = str(random.randrange(1, 28))
if len(dzien) == 1:
    dzien = '0' + dzien

if rokUrodzenia[1] == '8':
    miesiac = rokUrodzenia[1] + miesiacUrodzenia[1]
elif rokUrodzenia[1] == '9':
    miesiac = miesiacUrodzenia
    if len(miesiac) == 1:
        miesiac = '0' + miesiac
elif rokUrodzenia[1] == '0':
    miesiac = 20 + int(miesiacUrodzenia)
    miesiac = str(miesiac)
elif rokUrodzenia[1] == '1':
    miesiac = 40 + int(miesiacUrodzenia)
    miesiac = str(miesiac)
elif rokUrodzenia[1] == '2':
    miesiac = 60 + int(miesiacUrodzenia)
    miesiac = str(miesiac)

cyfraKontrolna = 0
if (int(rok[0]) * 1) / 10 < 1:
    cyfraKontrolna += int(rok[0]) * 1
else:
    cyfraKontrolna += (int(rok[0]) * 1) % 10

if (int(rok[1]) * 3) / 10 < 1:
    cyfraKontrolna += int(rok[1]) * 3
else:
    cyfraKontrolna += (int(rok[1]) * 3) % 10

if (int(miesiac[0]) * 7) / 10 < 1:
    cyfraKontrolna += int(miesiac[0]) * 7
else:
    cyfraKontrolna += (int(miesiac[0]) * 7) % 10

if (int(miesiac[1]) * 9) / 10 < 1:
    cyfraKontrolna += int(miesiac[1]) * 9
else:
    cyfraKontrolna += (int(miesiac[1]) * 9) % 10

if (int(dzien[0]) * 1) / 10 < 1:
    cyfraKontrolna += int(dzien[0]) * 1
else:
    cyfraKontrolna += (int(dzien[0]) * 1) % 10

if (int(dzien[1]) * 3) / 10 < 1:
    cyfraKontrolna += int(dzien[1]) * 3
else:
    cyfraKontrolna += (int(dzien[1]) * 3) % 10

if (int(plec[0]) * 7) / 10 < 1:
    cyfraKontrolna += int(plec[0]) * 7
else:
    cyfraKontrolna += (int(plec[0]) * 7) % 10

if (int(plec[1]) * 9) / 10 < 1:
    cyfraKontrolna += int(plec[1]) * 9
else:
    cyfraKontrolna += (int(plec[1]) * 9) % 10

if (int(plec[2]) * 1) / 10 < 1:
    cyfraKontrolna += int(plec[2]) * 1
else:
    cyfraKontrolna += (int(plec[2]) * 1) % 10

if (int(plec[3]) * 3) / 10 < 1:
    cyfraKontrolna += int(plec[3]) * 3
else:
    cyfraKontrolna += (int(plec[3]) * 3) % 10


if cyfraKontrolna / 10 > 1:
    cyfraKontrolna = 10 - (cyfraKontrolna % 10)
if cyfraKontrolna == 10:
    cyfraKontrolna = 0



pesel = rok+miesiac+dzien+plec+str(cyfraKontrolna)

print("Data urodzenia: ",rokUrodzenia,"-",miesiacUrodzenia,"-",dzien,sep="")
if int(plec[3])%2==0:
    print("plec:", "kobieta")
else:
    print("plec:","mezczyzna")

print("PESEL -", pesel)