import math


def powerof4(n):
    return type(n) is int and n > 0 and math.log(n, 4).is_integer()
