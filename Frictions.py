from math import gcd


class Fraction:
    def __init__(self, numerator: int = 0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __eq__(self, o):
        return self.denominator == o.denominator and self.numerator == o.numerator



if __name__ == '__main__':
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 2)

    f2 += f1
    print(f2)