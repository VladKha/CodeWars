def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())
