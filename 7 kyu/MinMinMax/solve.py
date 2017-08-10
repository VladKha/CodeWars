def minMinMax(arr):
    a = sorted(arr)
    i = 0
    while abs(a[i] - a[i+1]) <= 1:
        i += 1
    return [a[0], a[i]+1, a[-1]]
