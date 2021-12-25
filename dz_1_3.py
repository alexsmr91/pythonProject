def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    # место для Вашего кода
    if (number % 10 == 1) and ((number < 10) or (number > 15)):
        phrase = ' процент'
    elif (1 < number % 10 <5) and ((number < 10) or (number > 15)):
        phrase = ' процента'
    else:
        phrase = ' процентов'

    return str(number)+phrase


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))