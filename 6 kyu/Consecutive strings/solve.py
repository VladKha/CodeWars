def longest_consec(arr, k):
    n = len(arr)
    if n == 0 or k > n or k <= 0:
        return ''

    longest = ''

    for i in range(0, n - k + 1):
        tmp = ''.join(arr[i:i + k])
        if len(tmp) > len(longest):
            longest = tmp

    return longest
