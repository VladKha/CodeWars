def day_and_time(minutes):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    hours, minutes = divmod(minutes, 60)
    day, hours = divmod(hours, 24)
    day %= 7
    return '{} {:02d}:{:02d}'.format(days[day], hours, minutes)
