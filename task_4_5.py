from utils import currency_rates_adv
from decimal import Decimal
import datetime as DT

def main(argv):
    program, code = argv
    kurs, date_value = currency_rates_adv(code)
    empty = bool(not kurs and not date_value)
    if empty or not isinstance(kurs, Decimal):
        raise TypeError("Валюта не найдена")
    if empty or not isinstance(date_value, DT.date):
        raise TypeError("Что то не так с датой")
    print(kurs, date_value)

    return 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        exit(main(sys.argv))
    else:
        raise TypeError("Ожидался символьный код валюты")

