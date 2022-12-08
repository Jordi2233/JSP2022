#!/usr/bin/env python3
import os


def main():
    os.system('clear')

    l = [2*x for x in range(1, 50)]

    # l = [5, 25, 55, 33]

    for num in l:
        if num % 3 == 0 and num % 5 == 0:
            print('SykBzyk')
        else:
            if num % 3 == 0:
                print('Syk')
            elif num % 5 == 0:
                print('Bzyk')
            else:
                print(num)

if __name__ == '__main__':
    main()
