from collections import defaultdict


def switch_dict(d):
    d_new = defaultdict(list)
    for k,v in d.items():
        d_new[v].append(k)
    return d_new
