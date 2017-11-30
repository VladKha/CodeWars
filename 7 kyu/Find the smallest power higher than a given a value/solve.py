def find_next_power(val, pow_):
    return int(val ** (1 / pow_) + 1) ** pow_
