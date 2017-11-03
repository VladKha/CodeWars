from collections import Counter


def solve(a, b):
    c_diff, c_b = Counter(a), Counter(b)
    c_diff.subtract(c_b)
    result = 0
    for k,v in c_diff.items():
        if v >= 0:
            result += v
        else:
            return 0
    return result
