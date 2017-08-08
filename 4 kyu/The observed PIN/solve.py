from itertools import product


def get_pins(observed):
    adjacent = ['08', '124', '1235', '236', '1457', '24568', '3569', '478', '05789', '689']
    return [''.join(p) for p in product(*(adjacent[int(x)] for x in observed))]
