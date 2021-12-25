def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    # место для написания кода
    sum = 0
    for numb in dataset:
        sum_dig = 0
        numb_dig = numb
        while numb_dig > 0:
            sum_dig = sum_dig + numb_dig % 10
            numb_dig = numb_dig // 10
        if (sum_dig % 7) == 0:
            sum = sum + numb

    return sum  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    # место для написания кода
    sum = 0
    for numb in dataset:
        sum_dig = 0
        numb_dig = numb + 17
        while numb_dig > 0:
            sum_dig = sum_dig + numb_dig % 10
            numb_dig = numb_dig // 10
        if (sum_dig % 7) == 0:
            sum = sum + numb + 17

    return sum  # Верните значение полученной суммы


my_list = []  # Соберите нужный список по заданию
for i in range(3,1000,2):
    my_list.append(i**3)
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)