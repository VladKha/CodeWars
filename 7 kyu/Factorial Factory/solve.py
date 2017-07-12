from functools import lru_cache


@lru_cache(None)
def factorial(n):
    if n < 0:
        return None
    if n in [0, 1]:
        return 1
    return factorial(n - 1) * n
