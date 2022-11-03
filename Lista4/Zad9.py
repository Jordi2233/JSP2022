import os
os.system('clear')

num = int(input("Enter number: "))

def factorial(n):
    fact = 1

    for i in range(n):
        i += 1
        fact *= i

    return fact

res = factorial(num)
print(f"Factorial number of {num} is: {res}")

