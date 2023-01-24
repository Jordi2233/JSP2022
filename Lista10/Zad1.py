#!/usr/bin/env python3
import os
from math import pi


class Circle():

    def circuit(self):
        return round(2 * pi * self.radius, 2)

    def area(self):
        return round(pi * self.radius ** 2, 2)

    def __init__(self, radius):
        self.radius = radius


def main():
    os.system('clear')
    Circle1 = Circle(5)
    print(Circle1.radius)
    print(Circle1.circuit)
    print(Circle1.area)


if __name__ == '__main__':
    main()
