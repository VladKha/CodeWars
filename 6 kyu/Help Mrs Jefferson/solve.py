def shortest_arrang(n):
    r = n // 2 + 2
    a = [i for i in range(r, 0, -1)]
    for i in range(r):
        for j in range(r + 1):
            if sum(a[i:j]) == n:
                return a[i:j]
    return [-1]
