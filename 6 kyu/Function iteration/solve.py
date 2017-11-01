def create_iterator(func, n):
    def f(x):
        x = func(x)
        for _ in range(n-1):
            x = func(x)
        return x
    return f
