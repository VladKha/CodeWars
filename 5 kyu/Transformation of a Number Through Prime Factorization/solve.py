import random
from collections import Counter


def is_probably_prime(n):
    if n > 1:
        for time in range(3):
            random_n = random.randint(2, n) - 1
            if pow(random_n, n - 1, n) != 1:
                return False
        return True
    return False


def is_prime(n):
    if is_probably_prime(n):
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return False


def prime_factors(n):
    result = []
    while n != 1:
        for i in range(2, n + 1):
            if is_prime(n):
                i = n
            if n % i == 0:
                result.append(i)
                n //= i
                break
    return result


def f(n):
    powers = Counter(prime_factors(n))
    terms = [power * value ** (power - 1) for value, power in powers.items()]
    result = 1
    for t in terms:
        result *= t
    return result
