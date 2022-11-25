import os
from termcolor import colored


def decimal(num: int) -> int:
    res = (num - (num % 10))
    return res


def hundredth(num: int) -> int:
    res = (num - (num % 100))
    return res


def thousand(num: int) -> int:
    res = (num - (num % 1000))
    return res


def decimal_number(num: int, nums: dict) -> str:
    if num < 100 and num not in nums:
        unit = num % 10
        key = decimal(num) / 10
        if num % 10 != 0 and num > 50:
            res = f'{nums[key]}dziesiąt {nums[unit]}'
        elif num >= 50:
            res = f'{nums[key]}dziesiąt'
        else:
            key = num % 10
            res = f'{nums[decimal(num)]} {nums[unit]}'
    else:
        res = nums[num]
    return res


def hundredth_number(num: int, nums: dict) -> str:
    if num != 200:
        decimal = decimal_number(num % 100, nums)
    else:
        decimal = 0
    if num >= 300 and num <= 400:
        key = hundredth(num) / 100
        res = f'{nums[key]}sta {decimal}'
    elif num > 400:
        key = hundredth(num) / 100
        res = f'{nums[key]}set {decimal}'
    elif num not in nums:
        key = hundredth(num)
        res = f'{nums[key]} {decimal}'
    else:
        key = hundredth(num)
        res = f'{nums[key]}'
    return res


def thousand_number(num: int, nums: dict) -> str:
    if num != 1000:
        hundredth = hundredth_number(num % 1000, nums)
        key = thousand(num)
        res = f'{nums[key]} {hundredth}'
    else:
        res = nums[num]
    return res


def from_num_to_word(user_number: int) -> str:

    numbers = {0: "zero", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem", 9: "dziewięć", 10: "dziesięć", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście",
               15: "piętnaście", 16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście", 19: "dziewiętnaście", 20: "dwadzieścia", 30: "trzydzieści", 40: "czterdzieści", 100: "sto", 200: "dwieście", 1000: "tysiąc"}

    if user_number > 100 and user_number < 1000:
        res = hundredth_number(user_number, numbers)
    elif user_number >= 1000 and user_number <= 1999:
        res = thousand_number(user_number, numbers)
    elif user_number < 100:
        res = decimal_number(user_number, numbers)
    else:
        res = "Wrong Number!"
    return res


def main():
    os.system('clear')
    try:
        x = 0
        while x <= 1999:

            res = from_num_to_word(x)
            os.system('clear')
            print(f'{res}')
            x += 1
        print(colored("Test passed!", color="green"))
    except:
        print(colored("Test failed!", color="red"))

    # num: int = int(input("Wprowadź liczbę z zakresu od 0 do 1999: "))
    # res = from_num_to_word(num)
    # print(f'{res}')


if __name__ == '__main__':
    main()
