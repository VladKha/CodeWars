def divisors(n):
    result = [i for i in range(2, n) if n % i == 0]
    if len(result) == 0:
        return '{} is prime'.format(n)
    else:
        return result
