#!/usr/bin/env python3
import os


def genetic_sequence(x: str) -> str:
    x = x.upper()
    res = ""

    key = {
        "A": "T",
        "C": "G",
        "T": "A",
        "G": "C"
    }
    for letter in x:
        if letter in key:
            letter = key[letter]
            res += letter
        else:
            res = ""
    res = res[::-1]
    return res


def main():
    os.system('clear')
    user_sequence: str = input("Enter sequence:")
    res = genetic_sequence(user_sequence)

    if len(res) == 0:
        print(f"Wrong sequence\n{res}")
    else:
        print(f"Genetic sequence\n{res}")


if __name__ == "__main__":
    main()
