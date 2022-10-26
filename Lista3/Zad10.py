from os import *
system('clear')

res =[]
tem = 0
for x in range(100, 400):
    x += 1
    if x % 2 == 0:
        x = str(x)
        for y in x:
            y = int(y)
            # if y % 2 == 0 and y != 0:
            if y % 2 == 0:
                tem += 1
            else:
                tem -= 1
            if tem == len(x):
                res.append(x)
        tem = 0
for i in res:
    if i != res[-1]:
        print(i, end=", ")
    else:
        print(i)

