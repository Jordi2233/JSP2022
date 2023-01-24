#!/usr/bin/env python3
import os
from itertools import combinations


class Sublists:
    def __init__(self, lst):
        self.lst = lst
        # self.result = []
        # for i in range(len(lst) + 1):
        #     for subset in combinations(lst, i):
        #         self.result.append(list(subset))

        self.result = list(map(lambda x: list(map(int,x)), map(lambda x: [j for i in x for j in i], map(lambda i: list(combinations(lst, i)), range(len(lst) + 1)))))


def main():
    os.system('clear')
    list1 = [1, 2, 3]
    sublists1 = Sublists(list1)
    print(f" {sublists1.lst} -> {sublists1.result}")


if __name__ == '__main__':
    main()
