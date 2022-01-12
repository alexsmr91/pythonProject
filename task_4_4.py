from utils import currency_rates_adv



kurs, date_value = currency_rates_adv("USD")
print(kurs, date_value)

kurs, date_value = currency_rates_adv("amd")
print(kurs, date_value)

kurs, date_value = currency_rates_adv("aud")
print(kurs, date_value)




"""
74.8355 2022-01-12
0.155019 2022-01-12
53.7918 2022-01-12

Process finished with exit code 0
"""

