#!/usr/bin/env -S python3
import numpy as np
import sys


if len(sys.argv) == 1:
    dane = [int(line) for line in sys.stdin]
else:
    dane = [int(x) for x in sys.argv[1:]]

# print(f"Dane: {dane}")

sred = np.average(dane)
war = np.var(dane)
odch = np.std(dane)
print(f"\nSrednia = {sred} \nWariancja = {war} \nOdchylenie standardowe = {odch}")
