import os, itertools
os.system('clear')

given_list = input("Enter list: ").split()
given_list = [float(num) for num in given_list]

def all_perms(arr):
    if len(arr) <=1:
        yield arr
    else:
        for perm in all_perms(arr[1:]):
            for i in range(len(arr)):
                # nb arr[0:1] works in both string and list contexts
                yield perm[:i] + arr[0:1] + perm[i:]

all_permutations = list(all_perms(given_list))
print(all_permutations)



# With built in function
# all_perms = list(itertools.permutations(given_list))
# print(all_perms)
