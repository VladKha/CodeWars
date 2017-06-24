def flatten(lst):
    result = []
    for a in lst:
        if type(a) is list:
            result += a
        else:
            result.append(a)
    return result
