def sort_array(a):
    odds = sorted(x for x in a if x % 2 != 0)
    return [x if x % 2 == 0 else odds.pop(0) for x in a]
