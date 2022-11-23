import os
from num2words import num2words


def main():
    os.system('clear')
    num: int = input("Enter the number: ")

    print(num2words(num))

if __name__ == '__main__':
    main()
