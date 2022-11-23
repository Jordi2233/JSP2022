import os


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
        10: "dziesięć"
    }


    res: str = numbers[user_number]

    return res

def main():
    os.system('clear')
    num: int = int(input("Wprowadź liczbę z zakresu od 0 do 1999: "))

    res = from_num_to_word(num)
    print(f'{res}')


if __name__ == '__main__':
    main()
