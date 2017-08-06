def expanded_form(n):
    parts = []
    s = str(n)
    point_pos = s.find('.')

    i = point_pos - 1
    for c in s[:point_pos]:
        if c != '0':
            parts.append(str(int(c) * 10 ** i))
        i -= 1

    i = 1
    for c in s[point_pos+1:]:
        if c != '0':
            parts.append('{}/{}'.format(c, 10 ** i))
        i += 1
    return ' + '.join(parts)
