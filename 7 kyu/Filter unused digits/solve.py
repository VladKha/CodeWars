def unused_digits(*args):
    used = str(args)
    return ''.join(d for d in '0123456789' if d not in used)
