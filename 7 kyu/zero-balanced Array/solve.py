from collections import Counter


def is_zero_balanced(arr):
    c = Counter(arr)
    return bool(arr) and all(c[i] == c[-i] for i in c)
