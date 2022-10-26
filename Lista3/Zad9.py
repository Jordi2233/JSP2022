from os import *
import numpy as np
system('clear')

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

arr = np.ones((m, n), dtype=int)
arr[m - 1, n - 1] = m * n
print(arr)
