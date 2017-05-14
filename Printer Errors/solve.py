def printer_error(s):
    return '{}/{}'.format(sum(1 for c in s if c in 'nopqrstuvwxyz'), len(s))
