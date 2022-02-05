class MyDivisionByZeroException(ZeroDivisionError):
    def __init__(self, txt):
        print(txt)


if __name__ == "__main__":
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    try:
        if b == 0:
            raise MyDivisionByZeroException('бесконечность ∞')
        print(a / b)
    except MyDivisionByZeroException:
        pass

