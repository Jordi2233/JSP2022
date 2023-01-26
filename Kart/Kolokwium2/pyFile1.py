#!/usr/bin/env python3
import os
import sys


def main():
    os.system('clear')
    is_palindrome = lambda line: line == line[::-1]
    try:
        with open(sys.argv[1], 'r') as f, open('palindromy.txt', 'w') as f1, open('nie_palindromy.txt', 'w') as f2:
            for line in f:
                line = line.strip()
                if is_palindrome(line):
                    f1.write(line + '\n')
                else:
                    f2.write(line + '\n')


    except FileNotFoundError:
        print("The specified file does not exist.")
    except:
        print("An error occurred.")


if __name__ == '__main__':
    main()
