def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    eng_rus_dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
        'zero': 'ноль'
    }
    val_low = value.lower()
    if val_low == value:
        return eng_rus_dict.get(value)
    else:
        return eng_rus_dict.get(val_low).capitalize()



print(num_translate("One"))
print(num_translate("eight"))
