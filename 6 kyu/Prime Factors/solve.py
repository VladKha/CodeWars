def prime_factors(n):
    result = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                result.append(i)
                n //= i
                break
    return result
