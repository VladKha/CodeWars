def unique_in_order(iterable):
    result = []

    for i in iterable:
        if len(result) == 0 or i != result[-1]:
            result.append(i)

    return result
