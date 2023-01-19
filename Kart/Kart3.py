#!/usr/bin/env python3
import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @staticmethod
    def add(c1, c2):
        return ComplexNumber(c1.real + c2.real, c1.imag + c2.imag)

    @staticmethod
    def sub(c1, c2):
        return ComplexNumber(c1.real - c2.real, c1.imag - c2.imag)

    @staticmethod
    def multiply(c1, c2):
        real = c1.real * c2.real - c1.imag * c2.imag
        imag = c1.real * c2.imag + c1.imag * c2.real
        return ComplexNumber(real, imag)

    @staticmethod
    def division(c1, c2):
        conjugate = ComplexNumber(c2.real, -c2.imag)
        numerator = ComplexNumber.multiply(c1, conjugate)
        denominator = ComplexNumber.multiply(c2, conjugate)
        return ComplexNumber(numerator.real / denominator.real, numerator.imag / denominator.real)

    @staticmethod
    def modul(c1):
        return ((c1.real ** 2) + (c1.imag ** 2)) ** 0.5

    @staticmethod
    def argument(c1):
        if c1.real > 0:
            return math.atan(c1.imag / c1.real)
        elif c1.real < 0 and c1.imag >= 0:
            return math.atan(c1.imag / c1.real) + math.pi
        elif c1.real < 0 and c1.imag < 0:
            return math.atan(c1.imag / c1.real) - math.pi
        elif c1.real == 0 and c1.imag > 0:
            return math.pi / 2
        elif c1.real == 0 and c1.imag < 0:
            return -math.pi / 2
        else:
            return None

# c1 = ComplexNumber(2, 5)
# c2 = ComplexNumber(1, 1)
# print(f'{ComplexNumber.add(c1, c2).real} + {ComplexNumber.add(c1, c2).imag}i')
# print(f'{ComplexNumber.sub(c1, c2).real} + {ComplexNumber.sub(c1, c2).imag}i')
# print(f'{ComplexNumber.multiply(c1, c2).real} + {ComplexNumber.multiply(c1, c2).imag}i')
# print(f'{ComplexNumber.division(c1, c2).real} + {ComplexNumber.division(c1, c2).imag}i')
# print(ComplexNumber.modul(c1))
# print(ComplexNumber.argument(c1))
