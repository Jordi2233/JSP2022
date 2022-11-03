import os
os.system('clear')

given_list = input("Enter list: ").split()
given_list = [float(num) for num in given_list]

mode = input("What do you want to do? (Sum, Multi, Both?): ").lower()

sum = 0
multi = 1

for i in given_list:
    sum += i
    multi *= i

if mode == "sum":
    print(sum)
elif mode == "multi":
    print(multi)
else:
    print(sum, multi)
