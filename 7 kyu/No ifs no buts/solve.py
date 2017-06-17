def no_ifs_no_buts(a, b):
    d = {
        a > b: 'is greater than',
        a < b: 'is smaller than',
        a == b: 'is equal to'
    }
    return '{} {} {}'.format(a, d[True], b)
