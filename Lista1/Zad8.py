import os as s

s.system("clear")

a = int((input("Wprowadź pierwszą liczbę: ")))
b = int(input("Wprowadź drugą liczbę: "))


while a > b:
    print("Wprowadź liczby tak aby a było mniejsze od b")
    a = int((input("Wprowadź pierwszą liczbę: ")))
    b = int(input("Wprowadź drugą liczbę: "))

Z = b%a

print(Z)

Z *= Z + 3

print(Z)
