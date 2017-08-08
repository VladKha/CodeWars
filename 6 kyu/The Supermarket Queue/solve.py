def queue_time(customers, n):
    tills = [0] * n
    for c in customers:
        min_till = min(enumerate(tills), key=lambda p: p[1])[0]
        tills[min_till] += c
    return max(tills)
