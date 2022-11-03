import os
os.system('clear')

def print_line(arr):
    print(' '.join([str(item) for item in arr]).center(35))

n = int(input("Enter number of Pascal Triangle levels: "))

line = [1]
print_line(line)

for i in range(n - 1):
    next_line = [1]
    for j in range(len(line) - 1):
        next_line.append(line[j] + line[j + 1])
    next_line.append(1)
    line = next_line
    print_line(line)






