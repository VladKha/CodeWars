from collections import deque


def dbl_linear(n):
    x = 1
    i = 0
    d2, d3 = deque(), deque()
    while i < n:
        d2.append(2 * x + 1)
        d3.append(3 * x + 1)
        x = min(d2[0], d3[0])
        if x == d2[0]:
            x = d2.popleft()
        if x == d3[0]:
            x = d3.popleft()
        i += 1
    return x
