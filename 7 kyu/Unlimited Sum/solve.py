def sum(*args):
    result = 0
    for e in args:
        if type(e) == int:
            result += e
    return result
