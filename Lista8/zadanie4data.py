def dzien(pesel, dzien, miesiac):
    if int(miesiac) == 1 or int(miesiac) == 3 or int(miesiac) == 5 or int(
            miesiac) == 7 or int(miesiac) == 8 or int(miesiac) == 10 or int(
        miesiac) == 12:
        if pesel[4] == "0" or pesel[4] == "1" or pesel[4] == "2" or pesel[4] == "3":
            if pesel[4] == "3":
                if pesel[5] == "0" or pesel[5] == "1":
                    dzien = pesel[4]+pesel[5]
                else:
                    return None
            else:
                dzien = pesel[4]+pesel[5]
        else:
            return None
    elif int(miesiac) != 2:
        if pesel[4] == "0" or pesel[4] == "1" or pesel[4] == "2" or pesel[4] == "3":
            if pesel[4] == "3":
                if pesel[5] == "0":
                    dzien = pesel[4]+pesel[5]
                else:
                    return None
            else:
                dzien = pesel[4] + pesel[5]
        else:
            return None
    elif int(pesel[1])%2 == 0: #jeżeli parzysty rok
        if pesel[4] == "0" or pesel[4] == "1" or pesel[4] == "2":
            if pesel[4] == "2":
                dzien = pesel[4] + pesel[5]
            else:
                if int(pesel[5]) <= 8:
                    dzien = pesel[4] + pesel[5]
        else:
            return None
    return dzien


def miesiac(pesel, miesiac):
    # 1800-1899
    if pesel[2] == '8' or pesel[2] == '9':
        if pesel[3] == '1':
            if pesel[2] == '8':
                miesiac = '01'
            else:
                miesiac = '11'
        elif pesel[3] == '2':
            if pesel[2] == '8':
                miesiac = '02'
            else:
                miesiac = '12'
        elif pesel[3] == '3':
            miesiac = '03'
        elif pesel[3] == '4':
            miesiac = '04'
        elif pesel[3] == '5':
            miesiac = '05'
        elif pesel[3] == '6':
            miesiac = '06'
        elif pesel[3] == '7':
            miesiac = '07'
        elif pesel[3] == '8':
            miesiac = '08'
        elif pesel[3] == '9':
            miesiac = '09'
        elif pesel[3] == '0':
            miesiac = '10'
    # 1900-1999
    elif pesel[2] == '0' or pesel[2] == '1':
        if pesel[3] == '1':
            if pesel[2] == '0':
                miesiac = '01'
            else:
                miesiac = '11'
        elif pesel[3] == '2':
            if pesel[2] == '0':
                miesiac = '02'
            else:
                miesiac = '12'
        elif pesel[3] == '3':
            miesiac = '03'
        elif pesel[3] == '4':
            miesiac = '04'
        elif pesel[3] == '5':
            miesiac = '05'
        elif pesel[3] == '6':
            miesiac = '06'
        elif pesel[3] == '7':
            miesiac = '07'
        elif pesel[3] == '8':
            miesiac = '08'
        elif pesel[3] == '9':
            miesiac = '09'
        elif pesel[3] == '0':
            miesiac = '10'
    # 2000-2099
    elif pesel[2] == '2' or pesel[2] == '3':
        if pesel[3] == '1':
            if pesel[2] == '2':
                miesiac = '01'
            else:
                miesiac = '11'
        elif pesel[3] == '2':
            if pesel[2] == '2':
                miesiac = '02'
            else:
                miesiac = '12'
        elif pesel[3] == '3':
            miesiac = '03'
        elif pesel[3] == '4':
            miesiac = '04'
        elif pesel[3] == '5':
            miesiac = '05'
        elif pesel[3] == '6':
            miesiac = '06'
        elif pesel[3] == '7':
            miesiac = '07'
        elif pesel[3] == '8':
            miesiac = '08'
        elif pesel[3] == '9':
            miesiac = '09'
        elif pesel[3] == '0':
            miesiac = '10'
    # 2100-2199
    elif pesel[2] == '4' or pesel[2] == '5':
        if pesel[3] == '1':
            if pesel[2] == '4':
                miesiac = '01'
            else:
                miesiac = '12'
        elif pesel[3] == '2':
            if pesel[2] == '4':
                miesiac = '02'
            else:
                miesiac = '12'
        elif pesel[3] == '3':
            miesiac = '03'
        elif pesel[3] == '4':
            miesiac = '04'
        elif pesel[3] == '5':
            miesiac = '05'
        elif pesel[3] == '6':
            miesiac = '06'
        elif pesel[3] == '7':
            miesiac = '07'
        elif pesel[3] == '8':
            miesiac = '08'
        elif pesel[3] == '9':
            miesiac = '09'
        elif pesel[3] == '0':
            miesiac = '10'
    # 2200-2299
    elif pesel[2] == '6' or pesel[2] == '7':
        if pesel[3] == '1':
            if pesel[2] == '6':
                miesiac = '01'
            else:
                miesiac = '11'
        elif pesel[3] == '2':
            if pesel[2] == '6':
                miesiac = '02'
            else:
                miesiac = '12'
        elif pesel[3] == '3':
            miesiac = '03'
        elif pesel[3] == '4':
            miesiac = '04'
        elif pesel[3] == '5':
            miesiac = '05'
        elif pesel[3] == '6':
            miesiac = '06'
        elif pesel[3] == '7':
            miesiac = '07'
        elif pesel[3] == '8':
            miesiac = '08'
        elif pesel[3] == '9':
            miesiac = '09'
        elif pesel[3] == '0':
            miesiac = '10'
    return miesiac


def rok(pesel, rok):
    if pesel[2] == '8' or pesel[2] == '9':
        rok = "18"+pesel[0]+pesel[1]
    elif pesel[2] == '0' or pesel[2] == '1':
        rok = "19"+pesel[0]+pesel[1]
    elif pesel[2] == '2' or pesel[2] == '3':
        rok = "20"+pesel[0]+pesel[1]
    elif pesel[2] == '4' or pesel[2] == '5':
        rok = "21"+pesel[0]+pesel[1]
    elif pesel[2] == '6' or pesel[2] == '7':
        rok = "22"+pesel[0]+pesel[1]
    return rok


def kontrolna(pesel, cyfraKontrolna):
    if (int(pesel[0]) * 1) / 10 < 1:
        cyfraKontrolna += int(pesel[0]) * 1
    else:
        cyfraKontrolna += (int(pesel[0]) * 1) % 10

    if (int(pesel[1]) * 3) / 10 < 1:
        cyfraKontrolna += int(pesel[1]) * 3
    else:
        cyfraKontrolna += (int(pesel[1]) * 3) % 10

    if (int(pesel[2]) * 7) / 10 < 1:
        cyfraKontrolna += int(pesel[2]) * 7
    else:
        cyfraKontrolna += (int(pesel[2]) * 7) % 10

    if (int(pesel[3]) * 9) / 10 < 1:
        cyfraKontrolna += int(pesel[3]) * 9
    else:
        cyfraKontrolna += (int(pesel[3]) * 9) % 10

    if (int(pesel[4]) * 1) / 10 < 1:
        cyfraKontrolna += int(pesel[4]) * 1
    else:
        cyfraKontrolna += (int(pesel[4]) * 1) % 10

    if (int(pesel[5]) * 3) / 10 < 1:
        cyfraKontrolna += int(pesel[5]) * 3
    else:
        cyfraKontrolna += (int(pesel[5]) * 3) % 10

    if (int(pesel[6]) * 7) / 10 < 1:
        cyfraKontrolna += int(pesel[6]) * 7
    else:
        cyfraKontrolna += (int(pesel[6]) * 7) % 10

    if (int(pesel[7]) * 9) / 10 < 1:
        cyfraKontrolna += int(pesel[7]) * 9
    else:
        cyfraKontrolna += (int(pesel[7]) * 9) % 10

    if (int(pesel[8]) * 1) / 10 < 1:
        cyfraKontrolna += int(pesel[8]) * 1
    else:
        cyfraKontrolna += (int(pesel[8]) * 1) % 10

    if (int(pesel[9]) * 3) / 10 < 1:
        cyfraKontrolna += int(pesel[9]) * 3
    else:
        cyfraKontrolna += (int(pesel[9]) * 3) % 10

    if cyfraKontrolna / 10 > 1:
        cyfraKontrolna = 10 - (cyfraKontrolna % 10)
    if cyfraKontrolna == 10:
        cyfraKontrolna = 0

    # if cyfraKontrolna == int(pesel[10]):
    #     print("pesel ", pesel, " jest prawidlowy!")
    # else:
    #     print("pesel ", pesel, " jest nieprawidlowy :(")
    return cyfraKontrolna