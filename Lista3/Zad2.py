from os import *
system('clear')

num = int(input("Wprowadź cyfrę: "))

# if num % 2 == 0:
#     print("Parzysta")
# else:
#     print("Nieparzysta")

num_check = {
    0: "Parzysta",
    1: "Nieparzysta"
}

print(num_check[num % 2])
