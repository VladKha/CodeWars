def namelist(names):
    l = [d['name'] for d in names]
    result = ', '.join(l[:-1])
    if len(l) > 1:
        result += ' & ' + l[-1]
    elif len(l) == 1:
        result = l[0]
    return result
