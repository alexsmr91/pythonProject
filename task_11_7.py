class ComplexNumbers:

    def __init__(self, a: int, b=0):
        self.a = a
        self.b = b

    def __repr__(self):
        if self.b > 0:
            return f'{self.a} + {(self.b if self.b !=1 else "")}i'
        elif self.b < 0:
            return f'{self.a} - {(-self.b if self.b != -1 else "")}i'
        else:
            return f'{self.a}'

    def __add__(self, other):
        return ComplexNumbers(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumbers(self.a*other.a-self.b*other.b, self.a*other.b + self.b*other.a)


if __name__ == '__main__':
    n1 = ComplexNumbers(1, -1)
    n2 = ComplexNumbers(3, 6)
    print(n1 * n2)
    print(n1 + n2)
