#!/usr/bin/env python3
import os


def main():
    os.system('clear')

    A = []
    A.append([1, 2])
    A.append({'jeden': '1', 'dwa': '2'})

    res = [str(1) for x in range(1, 97)]

    A[1]['jeden'] = int(''.join(res))


    print(A)

if __name__ == '__main__':
    main()
