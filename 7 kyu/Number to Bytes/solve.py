def to_bytes(n):
    L = 8
    s = bin(n)[2:]
    s = s.rjust(len(s) + L - 1 - (len(s) - 1) % 8, '0')
    return [s[i:i+L] for i in range(0, len(s), L)]
