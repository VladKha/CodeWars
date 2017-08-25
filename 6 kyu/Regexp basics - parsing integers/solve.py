import re


def to_integer(s):
    if re.match(r'\A[+-]?((0b[01]+)|(0o[0-7]+)|(0x[\da-fA-F]+)|\d+)\Z', s):
        sign = 1
        if s[0] in '-+':
            sign = int(s[0] + '1')
            s = s[1:]
        base = {'0b': 2, '0o': 8, '0x': 16}.get(s[:2], 10)
        return sign * int(s, base)
    return None
