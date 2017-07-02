import re


def reverse(s):
    parts = re.findall(r'[a-zA-Z.]+|\s+', s)
    return ''.join(reversed(parts))
