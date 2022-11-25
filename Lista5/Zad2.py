import os

def decimal(num: int) -> int:
    res = (num - (num % 10))
    return res

def from_num_to_word(user_number: int) -> str:

    numbers = {
        1: "jeden",
        2: "dwa",
        3: "trzy",
        4: "cztery",
        5: "pięć",
        6: "sześć",
        7: "siedem",
        8: "osiem",
        9: "dziewięć",
        10: "dziesięć",
        11: "jedenaście",
        12: "dwanaście",
        13: "trzynaście",
        14: "czternaście",
        15: "piętnaście",
        16: "szesnaście",
        17: "siedemnaście",
        18: "osiemnaście",
        19: "dziewiętnaście",
        20: "dwadzieścia",
        30: "trzydzieści",
        40: "czterdzieści",
        100: "sto",
        1000: "tysiąc"
    }

    if user_number < 100 and user_number not in numbers:
        if user_number % 10 != 0 and user_number >= 50:
            key = decimal(user_number) / 10
            unit = user_number % 10
            res = f'{numbers[key]}dziesiąt {numbers[unit]}'
        else:
            key = user_number % 10
            res = f'{numbers[decimal(user_number)]} {numbers[key]}'
    else:
        res: str = numbers[user_number]
    return res


def main():
    os.system('clear')
    num: int = int(input("Wprowadź liczbę z zakresu od 0 do 1999: "))

    res = from_num_to_word(num)
    print(f'{res}')


if __name__ == '__main__':
    main()
