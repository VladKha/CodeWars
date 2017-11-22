def sum_nested(lst):
    return sum(sum_nested(x) if isinstance(x, list) else x for x in lst)
