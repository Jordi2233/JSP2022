import random
i = 1
file = open('PESEL.txt', 'w+')

while i <= 10:
    pesel = str(random.randrange(10000000000,99999999999))
    file.write(pesel+'\n')
    i += 1

file.close()
