import os
os.system('clear')

num: int = int(input("Enter number: "))

def factorial(n: int) -> int:
    fact = 1

    for i in range(1, n + 1):
        
        fact *= i

    return fact

res = factorial(num)
print(f"Factorial number of {num} is: {res}")

