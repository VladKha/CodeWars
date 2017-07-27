from collections import Counter


def stray(arr):
    return Counter(arr).most_common()[-1][0]
