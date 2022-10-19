from os import *
system('clear')

arr = []

for i in range(0, 100, 3):
    arr.append(i)

print("Array before del: ", "\n", arr, "\n")

del arr[4:len(arr):3]

print("Array after del: ", "\n", arr, "\n")
