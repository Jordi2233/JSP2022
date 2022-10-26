from os import *
system('clear')

n = int(input("Enter the last element of the Fibonacci sequence: "))

fib_arr = [0, 1, 1]


f_len = len(fib_arr)

for x in range(f_len, n):
    fib_arr.append(fib_arr[x-1] + fib_arr[x-2])


for x in range(len(fib_arr)):
    system("sleep 0.2")
    print(str(x + 1) + ") ", fib_arr[x])



