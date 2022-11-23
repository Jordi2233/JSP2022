import os

def from_str_to_num(user_str: str):
    user_str = user_str.lower()
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
        if user_str not in [wrong for wrong in wrongs]:
            if user_str not in [number for number in numbers]:
                if "teen" in user_str:
                    user_str = user_str[0:len(user_str) - 4]
                    res = numbers[user_str] + 10
                elif "ty" in user_str:
                    if " " in user_str:
                        user_str = user_str.split()
                        res = numbers[user_str[0]] + numbers[user_str[1]]
                    else:
                        user_str = user_str[0:len(user_str) - 2]
                        res = numbers[user_str] * 10
            else:
                res = numbers[user_str]
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


