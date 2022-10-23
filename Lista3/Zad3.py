from os import *
from math import *
system('clear')


def quadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if a == 0:
        x1 = x2 = "The equation is not quadratic"
    else:
        if d > 0:
            x1 = ((-b + sqrt(d)) / (2 * a))
            x2 = ((-b - sqrt(d)) / (2 * a))
        elif d == 0:
            x1 = x2 = (-b / 2 * a)
        else:
            x1 = x2 = "There are no real solutions"
    if x1 == x2:
        return x1
    else:
        return x1, x2

print("Enter numbers (Rational numbers with '.')")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

res = quadratic(a, b, c)

if type(res) is str:
    print(res)
else:
    print("Possible roots:", res)

# Examples:
# 1, 4, 3
# -4.5 0 4.5
# 25 2 2
# 0 3 3
