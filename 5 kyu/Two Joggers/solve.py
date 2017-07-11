from math import gcd


def nbr_of_laps(x, y):
    distance = (x * y) // gcd(x, y)
    return [distance // x, distance // y]
