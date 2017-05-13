def array_diff(a, b):
    y = set(b)
    return [x for x in a if x not in y]
