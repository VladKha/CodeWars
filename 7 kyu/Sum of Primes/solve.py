def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def sum_primes(lower, upper):
    result = 0
    for n in range(lower, upper + 1):
        if is_prime(n):
            result += n
    return result
