def remove_chars(s):
    return ''.join(c for c in s if c.isalpha() or c == ' ')
