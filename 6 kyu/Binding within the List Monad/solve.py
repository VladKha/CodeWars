def bind(lst, func):
    result = []
    for x in lst:
        result += func(x)
    return result
