from calendar import isleap


def year_days(year):
    return "{} has {} days".format(year, isleap(year) + 365)
