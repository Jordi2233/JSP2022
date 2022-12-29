#!/usr/bin/env python3
import os
from timing import timing
import functools


@timing
def fibonacci_1(n: int) -> int:
    res = [0, 1]

    for i in range(2, n + 1):
        res.append(res[i - 1] + res[i - 2])

    print(res)

# @timing


@functools.lru_cache()
def fibonacci_rec(n: int) -> int:

    res = []
    
    if n == 0:
        print(0)
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        res = fibonacci_rec(n-2) + fibonacci_rec(n-1)
        print(res)
        return res


def main():
    os.system('clear')

    n = int(input('Podaj n: '))

    timing(fibonacci_rec)(n)
    fibonacci_1(n)


if __name__ == '__main__':
    main()
