from collections import Counter


def find_the_missing_tree(trees):
    return Counter(trees).most_common()[-1][0]
