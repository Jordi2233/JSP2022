#!/usr/bin/env python3
import os
from itertools import combinations


class Sublists:
    def __init__(self, lst):
        self.result = []
        self.lst = lst
        for i in range(len(lst) + 1):
            for subset in combinations(lst, i):
                self.result.append(list(subset))


def main():
    os.system('clear')
    list1 = [1, 2, 3]
    sublists1 = Sublists(list1)
    print(f" {sublists1.lst} -> {sublists1.result}")


if __name__ == '__main__':
    main()
