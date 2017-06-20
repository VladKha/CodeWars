def narcissistic(n):
    s = str(n)
    return sum(int(x) ** len(s) for x in s) == n
