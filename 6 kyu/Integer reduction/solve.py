def solve(n,k):
    s = str(n)
    prev = 0
    removed = 0
    for _ in range(k):
        for i in range(prev, len(s)-1):
            if s[i+1] < s[i]:
                s = s[:i] + s[i+1:]
                prev = max(0, i - 1)
                removed += 1
                break
            prev = i
    return s[:len(s)-(k-removed)]
