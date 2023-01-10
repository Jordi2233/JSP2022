import random
import datetime
                    # generowanie prawidłowych, bo przy losowych ciężko było trafić na poprawny do zadania 8.4
def pesel():
    m = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]              # wagi kolejnych cyfr w peselu
    time = datetime.datetime.now()
    year = str(time.year)[2:]
    month = time.month + 20                         # na podstawie dzisiejszej daty (po 2000 wiec +20)
    if time.day < 10:
        day = "0" + str(time.day)
    else:
        day = str(time.day)
    pesele = []
    for i in range(11):                             # 10 peseli
        suma = 0                                    # na potrzeby cyfry 11 [kontrolnej]
        pesel = year + str(month) + day        # data na poczatku peselu
        for k in range(4):                          # generowanie 4 kolejnych cyfr w peselu
            pesel += str(random.randint(0, 9))

        for j in range(10):                         # obliczanie sumy na podstawie wag
            suma += int(pesel[j])*m[j]
        pesele.append(pesel + str(suma)[-1])        # wpisywanie peselu z cyfra kontrolna na koniec
    return pesele                                   # zwracanie listy peseli


with open("PESEL.txt", 'w') as f:
    f.write("".join([str(pesel)+"\n" for pesel in pesel()]))    # wpisywanie peselu z listy