#!/usr/bin/env python3
import os


class ThreeSum:
    def __init__(self, numbers):
        self.numbers = numbers

    # def find_triplets(self):
    #     triplets = []
    #     for i in range(len(self.numbers)):
    #         for j in range(i+1, len(self.numbers)):
    #             for k in range(j+1, len(self.numbers)):
    #                 if self.numbers[i] + self.numbers[j] + self.numbers[k] == 0:
    #                     triplets.append(
    #                         [self.numbers[i], self.numbers[j], self.numbers[k]])
    #     return triplets

    def find_triplets(self):
        return list(map(lambda x: [self.numbers[x[0]], self.numbers[x[1]], self.numbers[x[2]]], filter(lambda x: self.numbers[x[0]] + self.numbers[x[1]] + self.numbers[x[2]] == 0, [(i, j, k) for i in range(len(self.numbers)) for j in range(i+1, len(self.numbers)) for k in range(j+1, len(self.numbers))])))


def main():
    os.system('clear')
    numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
    print(f" {numbers} -> {ThreeSum(numbers).find_triplets()}")


if __name__ == '__main__':
    main()
