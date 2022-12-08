#!/usr/bin/env python3
import os


def by_one(word: str):

    res = 0
    vowel = 0
    vowels = ['A', 'Ą', 'E', 'Ę', 'I', 'O', 'U', 'Y']

    for letter in word:
        if letter in vowels:
            vowel += 1
    if vowel % 2 == 0 and vowel != 0:
        res += 2
    else:
        res += 1
    return res


def pkt(words: str) -> int:
    words = words.split()
    words = [x.upper() for x in words]
    res = 0
    for word in words:
        res += by_one(word)
    return res


def main():
    os.system('clear')
    res = pkt('Ala ma kota')

    print(res)



if __name__ == '__main__':
    main()
