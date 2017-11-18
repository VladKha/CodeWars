from collections import Counter


def example_sort(arr, example_arr):
    c = Counter(arr)
    result = []
    for x in example_arr:
        result += [x] * c[x]
    return result
