from datetime import datetime
from get_datetime_now import get_datetime_now

def get_day_of_week_now():
    datetime_now = get_datetime_now()
    return datetime.strftime(datetime_now, "%A")