#!/usr/bin/env python3
import os


def is_perfect(n): return sum(divisors(n)) == 2*n


def divisors(n): return [x for x in range(1, n+1) if n % x == 0]


def is_prime(n): return n > 1 and all(
    n % i for i in range(2, int(n ** (1/2)) + 1))


def main():
    os.system('clear')
    while True:
        try:
            n = int(input("Enter a natural number: "))
            if n < 0:
                raise ValueError
            divs = divisors(n)
            print("Divisors of {}: {}".format(n, divs))
            print("The number is prime.") if is_prime(n) else None
            print("The number is perfect.") if is_perfect(n) else None
            break
        except ValueError:
            print("Please enter a natural number.")


if __name__ == '__main__':
    main()
