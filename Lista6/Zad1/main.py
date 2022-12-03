#!/usr/bin/env python3
import os
import triangle as t


def main():
    os.system('clear')

    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    perimeter = t.perimeter(a, b, c)
    print(f"L = {perimeter}")

    area = t.area(a, b, c)
    print(f"P = {area}")

    triangle_type = t.kind(a, b, c)
    print(f"Type by sides: {triangle_type}")

    triangle_angle = t.angle(a, b, c)
    print(f"Type by angle: {triangle_angle}")


if __name__ == '__main__':
    main()
