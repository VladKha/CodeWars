from functools import lru_cache


@lru_cache(None)
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(x):
    for i in range(2, x+1):
        if is_prime(i):
            yield i
