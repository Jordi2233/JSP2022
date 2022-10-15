import numpy as np
from termcolor import colored
import os as s

s.system("clearrr")

colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

arr = np.arange(5 * 5).reshape(5, 5)

for color in colors:
    if (color == "grey"):
        print(colored(color, color, "on_white"),":\n", colored(arr, color, "on_white"), "\n")
    else:
        print(colored(color, color),":\n", colored(arr, color), "\n")
