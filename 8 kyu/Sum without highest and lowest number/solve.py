def sum_array(a):
    if not a or len(a) <= 1:
        return 0
    return sum(a) - min(a) - max(a)
