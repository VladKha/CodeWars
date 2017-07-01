import random


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


def f(n):
    max_prime, max_evens = 0, 0
    for i in range(n - 1, 1, -1):
        if len(str(i)) - 1 <= max_evens:
            break

        num_evens = sum(j in '02468' for j in str(i))
        if num_evens > 1 and is_prime(i):
            if num_evens > max_evens:
                max_prime = i
                max_evens = num_evens
    return max_prime
