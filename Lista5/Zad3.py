import os


def value(r: str) -> int:
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def romanToDecimal(user_number: str) -> int:
    res = 0
    i = 0

    while (i < len(user_number)):

        s1 = value(user_number[i])

        if (i + 1 < len(user_number)):

            s2 = value(user_number[i + 1])

            if (s1 >= s2):

                res = res + s1
                i = i + 1
            else:

                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res


def main():
    os.system('clear')
    user_number = input("Enter Roman number: ").upper()
    print(romanToDecimal(user_number))


if __name__ == '__main__':
    main()
