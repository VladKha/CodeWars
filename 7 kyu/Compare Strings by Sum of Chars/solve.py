def get_sum(s):
    if not s:
        return 0

    result = 0
    for c in s:
        if c.isalpha():
            result += ord(c.upper())
        else:
            result = 0
            break
    return result


def compare(s1, s2):
    return get_sum(s1) == get_sum(s2)
