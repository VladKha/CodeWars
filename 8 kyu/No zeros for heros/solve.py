def no_boring_zeros(n):
    if n == 0:
        return 0
    return int(str(n).strip('0'))
