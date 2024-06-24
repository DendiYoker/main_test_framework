import datetime


def now(time_format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime(time_format)
