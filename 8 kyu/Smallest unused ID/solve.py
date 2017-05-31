def next_id(a):
    i = 0
    set_a = set(a)
    while i in set_a:
        i += 1
    return i
