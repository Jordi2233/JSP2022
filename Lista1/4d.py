import numpy as np
from termcolor import colored
import os as s


s.system("clear")
x = 4
y = 5
m = 0

a = np.arange(x * y).reshape(x, y)
b = []
c = []

for i in range(0, x*y):
    b.append(i)

for j in range(0, x):
    c.append(b[m:m+5])
    m += 5

for i in c:
    print(i, end="\n")

print("\n", a)
