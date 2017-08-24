def climb(n):
    result = []
    while n:
        result.append(n)
        n //= 2
    return result[::-1]
