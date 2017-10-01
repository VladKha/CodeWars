def capitalize(s, ind):
    ind = set(ind)
    return ''.join(c.upper() if i in ind else c for i,c in enumerate(s))
