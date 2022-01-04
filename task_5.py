import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    list_out = []
    for i in range(count):
        list_out.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')

    return list_out



# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
def get_jokes_adv(count: int, uniq_flag=False) -> list:
    """ Функция возвращает count шуток, если задан uniq_flag = True, то шутки уникальны

    :param count: Количество шуток
    :param uniq_flag: Флаг уникальностти шуток
    :return: Возвращает список шуток
    """

    # пишите реализацию здесь
    list_out = []
    if uniq_flag:
        count = min(len(nouns), len(adverbs), len(adjectives))
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        for i in range(count):
            list_out.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    else:
        for i in range(count):
            list_out.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return list_out



print(get_jokes_adv(2))
print(get_jokes_adv(10, uniq_flag=False))
print(get_jokes_adv(10, True))


