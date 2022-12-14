#!/usr/bin/env python3
import os

from collections import Counter


def look_and_say(n):
    # initialize the first term of the sequence
    prev_term = "1"

    # loop for n iterations, starting from the second term of the sequence
    for i in range(2, n+1):
        # create a Counter object to count the number of each digit in the previous term
        c = Counter(prev_term)

        # initialize the current term as an empty string
        curr_term = ""

        # loop through the digits and their counts in the previous term
        for digit, count in c.items():
            # add the count and digit to the current term
            curr_term += str(count) + digit

        # set the current term as the previous term for the next iteration
        prev_term = curr_term

    # return the nth term of the sequence
    return prev_term


def main():
    os.system('clear')


if __name__ == '__main__':
    main()
