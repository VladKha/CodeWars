def solve(s):
    max_len, tmp_len = 0, 0
    for c in s:
        if c in 'aeiou':
            tmp_len += 1
        else:
            max_len = max(max_len, tmp_len)
            tmp_len = 0
    return max_len
