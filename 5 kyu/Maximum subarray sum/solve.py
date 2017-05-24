def maxSequence(a):
    if len(a) == 0:
        return 0

    n = len(a)
    dp = {}

    for i in range(n):
        dp[(i, i)] = a[i]

    for i in range(n):
        for j in range(i + 1, n):
            dp[(i, j)] = dp[(i, j-1)] + dp[(j, j)]

    max_key = max(dp, key=lambda key: dp[key])
    return dp[max_key]
