def count_number(n, x):
    count = 0

    for i in range(1, min(n + 1, x + 1)):
        a, b = divmod(x, i)
        if a <= n and b == 0:
            count += 1

    return count
