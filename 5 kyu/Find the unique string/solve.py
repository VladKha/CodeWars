from collections import defaultdict


def find_uniq(a):
    d = {}
    c = defaultdict(int)
    for e in a:
        t = frozenset(e.strip().lower())
        d[t] = e
        c[t] += 1

    return d[next(filter(lambda k: c[k] == 1, c))]
