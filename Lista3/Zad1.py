from os import *
system('clear')


letter = input("Podaj literę: ")
letter = letter.upper()

vowels = ['A', 'E', 'I', 'O', 'U', 'Ó', 'Y', 'Ą', 'Ę']
check = 0


for vowel in vowels:
    if letter == vowel:
        check += 1

if check == 1:
    print("Samogłoska")
else:
    print("Spółgłoska")
