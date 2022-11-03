import os
os.system('clear')

def nth_element(n, a1=1, q=2):
    an = a1 * (q**(n-1))
    return an

n = float(input("Enter the nth element of the sequence: "))
a1 = float(input("Enter first element of the sequence: "))
q = float(input("Enter product value of the sequence: "))


print(nth_element(n, a1, q))
