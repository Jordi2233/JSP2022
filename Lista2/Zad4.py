from os import *

system("clear")

text = input("Podaj napis: ")

text = list(text)

for i in range(len(text) - 1):
    i += 1
    if text[i] == text[0]:
        text[i] = "$"


text = "".join(text)
print(text)
