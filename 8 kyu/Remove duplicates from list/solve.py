from collections import OrderedDict


def distinct(seq):
    return list(OrderedDict.fromkeys(seq))
