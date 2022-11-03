import os
os.system('clear')

n = int(input("Enter the number of elements in the harmonic sequence: "))

harmonic = []

for i in range(n - 1):
    i += 1
    item = 1/i
    harmonic.append(round(item, 6))

harmonic_sum = round(sum(harmonic), 6)

print(f"Sum of {n} elements in harmonic sequence is: {harmonic_sum}")
