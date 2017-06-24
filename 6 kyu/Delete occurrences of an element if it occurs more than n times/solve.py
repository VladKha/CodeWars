from collections import defaultdict


def delete_nth(order, max_e):
    d = defaultdict(int)
    result = []
    for i in order:
        if d[i] < max_e:
            result.append(i)
            d[i] += 1
    return result
