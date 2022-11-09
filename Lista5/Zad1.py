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
    "thirteen": 13,
    "eighteen": 18,
    "twenty": 20,
    "thirty": 30,
    "fifty": 50
    }


    res = "Wrong number! Try Again!\n"

    wrongs = ["oneteen", "twoteen", "threeteen", "onety", "twoty", "threety"]
    try:
        if str not in [wrong for wrong in wrongs]:
            if str not in [number for number in numbers]:
                if "teen" in str:
                    str = str[0:len(str) - 4]
                    res = numbers[str] + 10
                elif "ty" in str:
                    if " " in str:
                        str = str.split()
                        res = numbers[str[0]] + numbers[str[1]]
                    else:
                        str = str[0:len(str) - 2]
                        res = numbers[str] * 10
            else:
                res = numbers[str]
    except:
        res

    return res


def main():
    os.system('clear')
    res = ""
    while True:
        num_str = input("Enter the number from 1 to 59 in words: ")
        res = from_str_to_num(num_str)
        print(res)
        if type(res) == int:
            break


if __name__ == '__main__':
	main()


