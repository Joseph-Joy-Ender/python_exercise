def seconds_since_midnight(hours_in_seconds, minute_in_seconds, seconds):
    hour = (60 * hours_in_seconds) * 60
    minutes = (60 * minute_in_seconds) + seconds
    return hour + minutes


print(seconds_since_midnight(13, 30, 45))
