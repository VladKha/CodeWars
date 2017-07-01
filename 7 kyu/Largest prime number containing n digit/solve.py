def is_prime(n):
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


def largest(n):
    if type(n) is not int or n < 1:
        return False
    i = int('9' * n)
    while True:
        if is_prime(i):
            return i
        i -= 1
