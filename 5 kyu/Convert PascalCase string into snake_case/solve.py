def to_underscore(s):
    s = str(s)
    result = s[0].lower()
    for c in s[1:]:
        if c.isupper():
            result += '_'
        result += c.lower()
    return result
