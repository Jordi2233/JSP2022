#!/usr/bin/env python3
import os
from timing import timing
from random import randint


@timing
def insert_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr

@timing
def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def number_generator(n: int) -> list:
    return [randint(0, 20) for x in range(n)]


def main():
    os.system('clear')
    arr = [number_generator(x) for x in range(100, 301, 100)]


    for i in arr:
        insert_sort(i)
        bubble_sort(i)

if __name__ == '__main__':
    main()
