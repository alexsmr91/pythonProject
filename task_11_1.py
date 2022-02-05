import re


class MyDate:
    day = None
    month = None
    year = None

    def __init__(self, date: str):
        day, month, year = MyDate.parser(date)
        if self.validator(day, month, year):
            self.day = day
            self.month = month
            self.year = year

    @classmethod
    def parser(cls, str_in: str):
        match = re.match(r'\b(\d{1,2})\-(\d{1,2})\-(\d{4,6}|\d{2})\b', str_in)
        if match and len(str_in) == len(match.group()):
            day, month, year = map(int, match.groups())
            return day, month, year
        else:
            return -1, -1, -1

    @staticmethod
    def validator(day, month, year):
        if month > 12 or month < 1:
            return False
        max_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        leap_year = (True if year % 4 == 0 else False)
        month_max = (max_days[month - 1] + 1 if leap_year and month == 2 else max_days[month - 1])
        return 1 <= day <= month_max


if __name__ == "__main__":
    my_dates = ('30-2-2020', '29-2-2021', '29-2-2020', '31-4-2020', '30-4-2020', '1-13-2020', '0-1-2020', '1-0-2020', 'a-1-2020', '1-1-20020', '1-1-2020 a')
    for st in my_dates:
        my_date = MyDate(st)
        print(f'"{st}" {my_date.day}.{my_date.month}.{my_date.year}')
