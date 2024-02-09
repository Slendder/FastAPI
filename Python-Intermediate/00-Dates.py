### Dates ###
from datetime import datetime, date, time, timedelta

now = datetime.now()
current_time = time()
year_2023 = datetime(2023, 1, 1)
current_date = date(2023, 12, 19)


def print_datetime(date):
    print(date.Calendar(date.year, w=2, l=1, c=6, m=3))
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.min)
    print(date.second)
    print(now.timestamp())
def print_time(current):
    print(current.hour())
    print(current.min())
    print(current.second())
def print_date(current):
    print(current.year())
    print(current.month())
    print(current.day())

diff = year_2023 - now
print(diff)
diff = year_2023.date() - current_date
print(diff)


## ? Time Delta!


start_timedelta = timedelta(200, 131, 231, weeks=10)
end_timedelta = timedelta(200, 131, 231, weeks=9)

print(start_timedelta - end_timedelta)
