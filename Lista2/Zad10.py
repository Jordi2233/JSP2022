from os import *
system('clear')

arr = [num for num in range(0, 100, 3)]


print(f"Array before del:\n{arr}\n")

del arr[4::3]

print(f"Array after del:\n {arr} \n")
