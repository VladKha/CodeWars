from collections import Counter


def find_uniq(a):
    return Counter(a).most_common()[-1][1]
