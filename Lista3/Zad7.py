from os import *
system('clear')

n = int(input("Enter the last element of the Fibonacci sequence: "))

fib_arr = [0, 1, 1]

for x in range(len(fib_arr), n):
    fib_arr.append(fib_arr[x-1] + fib_arr[x-2])

print(f"Last element of your sequence: {fib_arr[n-1]}")

# for x in range(len(fib_arr)):
#     system("sleep 0.2")
#     print(  f"{x + 1} ) \t{fib_arr[x]}" )



