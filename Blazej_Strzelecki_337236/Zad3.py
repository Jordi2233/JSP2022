#!/usr/bin/env python3
import os
from math import pi


def f(r: float, m: str) -> float:
    if m == 'mm':
        res = pi * ((r / 1000) ** 2)
    elif m == 'cm':
        res = pi * ((r / 100) ** 2)
    else:
        res = pi * (r ** 2)

    return res


def main():
    os.system('clear')
    print(f(1, 'mm'))


if __name__ == '__main__':
    main()
