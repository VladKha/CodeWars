import heapq


def two_highest(l):
    return heapq.nlargest(2, set(l)) if type(l) == list else False
