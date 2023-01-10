import numpy as np
import sys

if len(sys.argv) == 1:
    dane = [int(line) for line in sys.stdin]
else:
    dane = sys.argv[1:]

sred = np.average(dane)
war = np.var(dane)
odch = np.std(dane)
print("\n","Srednia = ", sred, "\n", "Wariancja = ", war, "\n" ,"Odchylenie standardowe = ", odch)