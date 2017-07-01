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


def pernicious(n):
    if n <= 0:
        return 'No pernicious numbers'
    n = int(n)
    result = []
    for i in range(1, n + 1):
        s = bin(int(i))[2:]
        if is_prime(sum(int(i) for i in s)):
            result.append(i)
    return result if result else 'No pernicious numbers'
