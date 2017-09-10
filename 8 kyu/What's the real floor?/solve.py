def get_real_floor(n):
    if n <= 0:
        return n
    return n - 1 - (n >= 13)
