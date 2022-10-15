import numpy as np
from termcolor import colored
import os as s

s.system("clear")

colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

a = np.arange(5 * 5).reshape(5, 5)

for x in colors:
    if (x == "grey"):
        print(colored(x, x, "on_white"),":\n", colored(a, x, "on_white"), "\n")
    else:
        print(colored(x, x),":\n", colored(a, x), "\n")
print(a.ndim)
