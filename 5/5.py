from get_day_of_week import get_day_of_week_now
from get_datetime_now import get_datetime_now

datetime_obj = get_datetime_now()
print(f"Текущая дата и время: {datetime_obj.strftime('%Y-%m-%d %H:%M:%S')}")
day_of_week = get_day_of_week_now()
print(f"Текущий день недели: {day_of_week}")