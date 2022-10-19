import os as s
from math import *
from cmath import *


s.system("clear")

z = complex(0, 1)

sin_z = sin(z)
cos_z = cos(z)

L_r = "Liczba rzeczysista z "
L_im = "Liczba zespolona z "

print("z =", z)

print()

print(L_r + "sin(z):" ,sin_z.real, "\n", L_im + "sin(z): ", sin_z.imag)

print()

print(L_r + "cos(z):", cos_z.real, "\n", L_im + "cos(z):", cos_z.imag)



test = sin_z**2 + cos_z**2
print("sin^2(z) + cos^2(z) =", test)
