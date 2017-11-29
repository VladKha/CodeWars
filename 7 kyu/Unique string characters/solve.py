def solve(a, b):
    s = set(a) & set(b)
    return ''.join(c for c in a + b if c not in s)
