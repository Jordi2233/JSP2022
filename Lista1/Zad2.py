from math import *
import os as s

s.system("clear")

a = 3
b = 4

k = 47

p = 1/2 * a * b * sin(k * pi / 180)

print(p)

# Zad3

a = int(input("Podaj pierwszy bok: "))
b = int(input("Podaj drugi bok: "))
k = int(input("Podaj kąt: "))

p = 1/2 * a * b * sin(k)
print(p)
