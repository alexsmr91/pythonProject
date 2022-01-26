import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """

    RE_MAIL = re.compile(r'\w+\@{1}\w+\.\w+')
    nd_list = re.split(r'\@{1}', email)
    if len(RE_MAIL.findall(email)) == 1 and len(nd_list) == 2:
        return {'username': nd_list[0], 'domain': nd_list[1]}
    else:
        msg = f'wrong email: {email}'
        raise ValueError(msg)


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrains,ru')
    email_parse('someone@geekbrains.russomeone.geekbrains.ru')
