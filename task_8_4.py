from functools import wraps


def val_checker(req=lambda x: x):
    def val_wrapper(func):
        @wraps(func)
        def wrapper(*args):
            for arg in args:
                try:
                    int(arg)
                except ValueError:
                    msg = f'wrong val {arg}'
                    raise ValueError(msg)
                if not req(arg):
                    msg = f'wrong val {arg}'
                    raise ValueError(msg)
            return func(*args)
        return wrapper
    return val_wrapper


@val_checker(lambda x: x >= 0)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
