from collections import Counter


def vampire_test(x, y):
    return Counter(str(x) + str(y)) == Counter(str(x * y))
