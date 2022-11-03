import os, math
os.system('clear')


num = int(input("Enter number: "))
mode = input("What do you want to do? (d2r/r2d): ")

def convert(num, mode):
    if mode =="d2r":
        res = num * (math.pi/180)
    elif mode == "r2d":
        res = num * (180/math.pi)
    else:
        res = "Wrong argument"
    return round(res, 3) 

print(convert(num, mode))
