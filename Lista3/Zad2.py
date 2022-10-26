from os import *
system('clear')

num = input("Enter number: ")

x = 1

while x != 0:

    if "." in num or "," in num:
        system("clear")
        print("Enter whole number")
        num = input("Enter number: ")
    else:
        num = int(num)
        x = 0


# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# num_check = {
#     0: "Even",
#     1: "Odd"
# }

# print(num_check[num % 2])

print(["Even", "Odd"][num % 2])
