import os, math
os.system('clear')

while True:
    nums = input("Enter two numbers to find GCD: ").split()
    nums = [int(num) for num in nums]

    if len(nums) == 2:
        os.system('clear')
        res = math.gcd(nums[0], nums[1])
        print(f"GCD of {nums[0]} and {nums[1]} is: {res}")
    else:
        os.system('clear')
        print("Not enough numbers! Try again!")

