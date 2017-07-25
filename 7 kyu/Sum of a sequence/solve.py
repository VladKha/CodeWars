def sequence_sum(a, b, step):
    n = (b - a) // step
    return 0 if n < 0 else (n + 1) * (n * step + 2 * a) // 2
