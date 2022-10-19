import os as s
from cmath import *

s.system("clear")

re = int(input("Wprowadź liczbę rzeczywistą: "))
im = int(input("Podaj jednostkę zespoloną: "))

z = complex(re, im)

print(z)

print(abs(z))

print(phase(z))
