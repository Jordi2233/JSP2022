from os import *
system('clear')

i = int(input("Enter number: "))

for num in range(10):
    num += 1
    if(num == 10):
        print(str(i) +" * "+ str(num) + " = ", i * num)
    else:
        print(str(i) +" * "+ str(num) + " =  ", i * num)



