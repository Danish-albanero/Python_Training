from time import time


def current_time_ms():
    return round(time() * 1000)
