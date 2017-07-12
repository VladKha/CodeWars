def nb_dig(n, d):
    return sum(str(k ** 2).count(str(d)) for k in range(n + 1))
