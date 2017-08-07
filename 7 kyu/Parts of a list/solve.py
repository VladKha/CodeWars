def partlist(a):
    return [(' '.join(a[:i]), ' '.join(a[i:])) for i in range(1, len(a))]
