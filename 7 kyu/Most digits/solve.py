def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))
