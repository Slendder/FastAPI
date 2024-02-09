### Dates ###
from datetime import datetime

now = datetime.now()


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.min)
    print(date.second)
    print(now.timestamp())


print(now)

year_2023 = datetime(2023, 1, 1)

if input("asda: ") != "adsa":
    print('asd')

print_date(year_2023)
