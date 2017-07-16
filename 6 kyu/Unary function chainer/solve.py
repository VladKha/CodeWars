def chained(functions):
    def f(x):
        for func in functions:
            x = func(x)
        return x
    return f
