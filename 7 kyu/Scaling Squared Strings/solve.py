def scale(s, k, n):
    result = ''
    for p in s.split():
        tmp = ''
        for i in range(len(p)):
            tmp += p[i] * k
        result += (tmp + '\n') * n
    return result.strip()
