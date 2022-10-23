from os import *
from re import findall
import maskpass
system('clear')

x = False
# passwd = input("Enter Password: ")
passwd = maskpass.askpass(mask="*")

while x != True:
    pass_len = len(passwd)
    if findall("[0-9]", passwd) and findall("[a-zA-Z]", passwd) and findall("[$#@]", passwd) and pass_len > 6 and pass_len <= 16:
        system("clear")
        print("Good password")
        x = True
    else:
        print("\n","Weak password. Try again.")
        # passwd = input("Enter Password: ")
        passwd = maskpass.askpass(mask="")

