#!/usr/bin/env python3
import os


def main():
    os.system('clear')

    K = (
        ('król', {2: 'królewna', 1: ['córka', 'wróbel']}, '5'), ('żółw', 'pies'))

    print(K[0][1][1][1])


if __name__ == '__main__':
    main()
