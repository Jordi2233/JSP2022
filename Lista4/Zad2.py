import os
os.system('clear')


def func(arr):
    arr = [*set(arr)]
    return arr

print(func([1, 1, 1, 2]))
