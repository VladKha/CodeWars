def sc(s):
    chars = set(s)
    return ''.join(c for c in s if c.swapcase() in chars)
