from collections import Counter


def duplicate_count(text):
    return sum(1 for _, n in Counter(text.lower()).items() if n > 1)
