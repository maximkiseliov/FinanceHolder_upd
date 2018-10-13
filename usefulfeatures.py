import time
import datetime


def current_date_plus_time():
    current_time = time.time()
    date = str(datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S'))
    return date
