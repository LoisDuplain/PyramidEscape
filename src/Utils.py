import time


def get_current_time_millis():
    return int(round(time.time() * 1000))


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
