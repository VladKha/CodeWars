UPSIDE_DOWN_DIGITS = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}


def is_upside_down_number(n):
    s = str(n)
    if all(c in UPSIDE_DOWN_DIGITS for c in s) and (not len(s) % 2 or s[len(s) // 2] not in "69"):
        return all(UPSIDE_DOWN_DIGITS[c] == s[-1-i] for i, c in enumerate(s[:len(s) // 2]))
    return False


def solve(a, b):
    return sum(is_upside_down_number(i) for i in range(a,b))
