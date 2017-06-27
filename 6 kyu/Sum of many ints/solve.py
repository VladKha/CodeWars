def f(n, m):
    a, b = divmod(n, m)
    return (a * m*(m-1) + (b+1)*b) / 2
