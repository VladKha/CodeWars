from functools import reduce


def logical_calc(array, op):
    return reduce(lambda x,y: {'OR': x or y, 'AND': x and y, 'XOR': x ^ y}[op], array)
