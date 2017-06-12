def first_non_consecutive(a):
    i = a[0]
    for e in a:
        if e != i:
            return e
        i += 1
    return None
