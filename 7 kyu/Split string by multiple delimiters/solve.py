def multiple_split(s, delimiters=()):
    result = []
    tmp = ''
    for ch in s:
        if ch not in delimiters:
            tmp += ch
        elif tmp != '':
            result.append(tmp)
            tmp = ''
    if tmp != '':
        result.append(tmp)
    return result
