def get_length_of_missing_array(arr):
    if not arr:
        return 0

    n = len(arr)
    sizes = [0 for _ in range(n)]
    for i in range(n):
        if not arr[i]:
            return 0
        sizes[i] = len(arr[i])
    sizes.sort()

    return (sizes[0] + sizes[-1]) * (n + 1) // 2 - sum(sizes)
