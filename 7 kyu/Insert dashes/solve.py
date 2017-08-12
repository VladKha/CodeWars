def insert_dash(num):
    odd = '13579'
    s = str(num)
    result = s[0]
    for i in range(1, len(s)):
        if s[i-1] in odd and s[i] in odd:
            result += '-'
        result += s[i]
    return result
