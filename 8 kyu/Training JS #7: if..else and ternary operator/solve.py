def sale_hotdogs(n):
    return (100 if n < 5 else 95 if 5 <= n < 10 else 90) * n
