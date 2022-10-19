from os import *
system("clear")


students = ["Kasia", "Basia", "Marek", "Darek"]

students.append("Józek")

students.extend(["Ania", "Basia"])

students.sort()

print(students)
print()
print(students[3])
print(students[:2])
print(students[-2:])
print()

for name in students:
    if name == "Basia":
        students.remove("Basia")

print(students)
print()
print(len(students))
print()
students = tuple(students)

print(students)
