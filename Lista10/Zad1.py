#!/usr/bin/env python3
import os
from math import pi


class Circle():

    def circuit(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

    def __init__(self, radius):
        self.radius = radius


def main():
    os.system('clear')
    Circle1 = Circle(5)
    print(Circle1.radius)
    print(round(Circle1.circuit(), 3))
    print(round(Circle1.area(), 3))


if __name__ == '__main__':
    main()
