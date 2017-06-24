def move_zeros(a):
    filtered = [x for x in a if x is False or x != 0]
    return filtered + [0] * (len(a) - len(filtered))
