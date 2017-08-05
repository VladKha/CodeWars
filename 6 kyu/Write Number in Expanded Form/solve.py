def expanded_form(n):
    divisor = 10 ** (len(str(n)) - 1)
    parts = []
    while n:
        p, n = divmod(n, divisor)
        if p:
            parts.append(str(p * divisor))
        divisor //= 10
    return ' + '.join(parts)
