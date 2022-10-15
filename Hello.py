from termcolor import colored
import os as s
s.system("clear")

number_of_prints = int(input("Number of prints: "))


for i in range(number_of_prints):
    if i % 2 == 0:
        print(colored("Hello World!", "blue"))
    else:
        print(colored("Hello Hell!", "yellow"))
