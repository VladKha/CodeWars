from functools import lru_cache


def nth_fib(n):
    return fibonacci(n-1)


@lru_cache(None)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
