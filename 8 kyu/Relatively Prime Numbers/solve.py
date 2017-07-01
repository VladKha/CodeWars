from fractions import gcd


def relatively_prime (n, l):
    return [x for x in l if gcd(n, x) == 1]
