def szyfr(w, p):       # A - 65 a - 97 z - 122 Z - 90
    z = ""
    for i in range(len(w)):
        if (ord(w[i]) >= 65 and ord(w[i]) <= 90) or (ord(w[i]) >= 97 and ord(w[i]) <= 122):
            if ord(w[i]) > 122 - p or (ord(w[i]) > 90 - p and ord(w[i]) < 97):
                z += chr(ord(w[i]) - 26 + p)
            else:
                z += chr(ord(w[i])+p)
        else:
            z += w[i]
    return z

def deszyfr(w, p):
    d = ""
    for i in range(len(w)):
        if(ord(w[i]) >= 65 and ord(w[i]) <= 90) or (ord(w[i]) >= 97 and ord(w[i]) <= 122):
            if ((ord(w[i]) < 97 + p and ord(w[i]) > 90 + p) or (ord(w[i]) < 65 + p)):
                d += chr(ord(w[i]) + 26 - p)
            else:
                d += chr(ord(w[i]) - p)
        else:
            d += w[i]
    return d