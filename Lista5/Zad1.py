import os

def from_str_to_num(str):
    str = str.lower()
    numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13
    }


    if "teen" in str and str != [x: for x in]:
        str = str[0:len(str) - 4]
        res = numbers[str] + 10
        # res = str
    else:
        res = numbers[str]

    return res


def main():
    os.system('clear')
    num_str = input("Enter the number from 1 to 59 in words: ")
    print(from_str_to_num(num_str))
    # from_str_to_num(num_str)


if __name__ == '__main__':
	main()
