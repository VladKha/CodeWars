def largest_sum(s):
    max_sum = 0
    tmp = 0
    for c in s:
        if c != '0':
            tmp += int(c)
        else:
            max_sum = max(max_sum, tmp)
            tmp = 0
    return max_sum
