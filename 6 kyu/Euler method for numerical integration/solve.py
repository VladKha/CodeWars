def euler(stop, step_size):
    f = lambda x: 5 + 2 * x + 3 * x ** 2
    n = int(stop // step_size)
    prev = 0
    for i in range(n + 1):
        prev += step_size * f(step_size * i)
    return prev
