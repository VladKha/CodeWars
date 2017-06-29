def last(*args):
    return args[-1] if not hasattr(args[-1], "__getitem__") else args[-1][-1]
