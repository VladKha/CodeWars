def find_digit(n, nth):
    if nth <= 0:
        return -1
    s = str(abs(n))
    return int(s[-nth]) if nth <= len(s) else 0
