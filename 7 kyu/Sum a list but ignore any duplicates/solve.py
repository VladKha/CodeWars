from collections import Counter


def sum_no_duplicates(l):
    c = Counter(l)
    return sum(k for k,v in c.items() if v == 1)
