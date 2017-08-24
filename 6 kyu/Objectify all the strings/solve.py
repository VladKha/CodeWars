def hashify(s):
    d = {}
    s += s[0]
    for i in range(len(s)-1):
        tmp = d.get(s[i])
        if tmp is None:
            d[s[i]] = s[i+1]
        elif type(tmp) == str:
            d[s[i]] = [tmp, s[i+1]]
        else:
            d[s[i]].append(s[i+1])
    return d
