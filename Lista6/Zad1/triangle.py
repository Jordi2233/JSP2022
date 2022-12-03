from math import sqrt


def check_triangle(a: float, b: float, c: float):
    if a + b > c or a == b == c:
        res = True
        return res
    else:
        res = "Invalid input: make sure a + b > c"
        return res


def perimeter(a: float, b: float, c: float) -> float:
    valid = check_triangle(a, b, c)
    if valid == True:
        res = a + b + c
        return res
    else:
        return valid


def area(a: float, b: float, c: float) -> float:
    valid = check_triangle(a, b, c)
    if valid == True:
        s = (a + b + c) / 2
        res = sqrt(s * (s - a) * (s - b) * (s - c))
        res = round(res, 2)
        return res
    else:
        return valid


def kind(a: float, b: float, c: float) -> str:
    valid = check_triangle(a, b, c)
    if valid == True:
        if a == b == c:
            res = "Equilateral triangle"
        elif a == b != c:
            res = "Isosceles triangle"
        else:
            res = "Scalene triangle"
        return res
    else:
        return valid

def angle(a: float, b: float, c: float):
    valid = check_triangle(a, b, c)
    if valid == True:
        if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
            res = "Rectangular triangle"
        elif  (b ** 2 + c ** 2 > a ** 2) and (a ** 2 + c ** 2 > b ** 2) and (a ** 2 + b ** 2 > c ** 2):
            res = "Acute triangle"
        else:
            res = "Obtuse triangle"
        return res
    else:
        return valid