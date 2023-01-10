def szyfrowanie(file, key):
    szyfr = ""
    for line in file:
        for i in line:
            if ((ord(i) >= 97) and (ord(i) <= (122 - key))) or ((ord(i) >= 65) and ord(i) <= (90 - key)):
                szyfr += chr(int(ord(i) + key))
            elif (int(ord(i) >= 97 and int(ord(i) <= 122))) or (int(ord(i) >= 65 and int(ord(i) <= 90))):
                szyfr += chr(int(ord(i) - 26 + key))
            else:
                szyfr += i
    return szyfr

def deszyfrowanie(file, key):
    deszyfr = ""
    for line in file:
        for i in line:
            if ((ord(i) >= 97 + key) and (ord(i) <= 122)) or ((ord(i) >= 65 + key) and ord(i) <= 90):
                deszyfr += chr(int(ord(i) - key))
            elif (int(ord(i) >= 97 and int(ord(i) <= 122))) or (int(ord(i) >= 65 and int(ord(i) <= 90))):
                deszyfr += chr(int(ord(i) + 26 - key))
            else:
                deszyfr += i
    return deszyfr