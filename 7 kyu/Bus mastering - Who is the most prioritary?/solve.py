def arbitrate(s, n):
    i = s.find('1') + 1
    return s[:i] + '0' * (n - i)

