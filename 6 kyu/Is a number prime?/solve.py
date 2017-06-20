import math


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    root = int(math.sqrt(n))
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True
