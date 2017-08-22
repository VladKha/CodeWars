from functools import reduce


def grow(arr):
    return reduce(lambda x,y: x*y, arr)
