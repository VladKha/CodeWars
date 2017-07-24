def candies(s):
    if not s or len(s) == 1:
        return -1
    return len(s) * max(s) - sum(s)
