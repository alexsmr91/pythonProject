from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        if len(args) > 0:
            msg = ''
            results = []
            for arg in args:
                res = func(arg)
                results.append(res)
                msg = f'{msg}, {func.__name__}({arg}: {type(arg)} = {res}: {type(res)})'
            msg = msg.strip(',')
            msg = msg.strip()
            print(msg)
            return (tuple(results) if len(results)>1 else results[0])
        else:
            raise TypeError(f"{func.__name__} missing 1 required positional argument: 'x'")
    return wrapper


@type_logger
def calc_cube(x):
    """
    Возведение числа в третью степень
    :param x: число
    :return: x ^ 3
    """
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5.1))
