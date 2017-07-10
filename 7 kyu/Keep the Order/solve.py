def keep_order(a, value):
    for i in range(len(a)):
        if value <= a[i]:
            return i
    return len(a)
