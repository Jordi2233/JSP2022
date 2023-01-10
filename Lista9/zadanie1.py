import numpy as np

A = np.array([[1, 2, 3, -2, -1],
              [3, 5, 5, -3, -9],
              [2, 3, 2, 0, -8],
              [2, 6, 7, -5, 1],
              [1, 2, 6, -4, -10]])
b = np.array([6,2,-5,17,12])
tab = np.linalg.solve(A,b)

print("x = ",tab[0])
print("z = ",tab[1])
print("y = ",tab[2])
print("t = ",tab[3])
print("u = ",tab[4])
