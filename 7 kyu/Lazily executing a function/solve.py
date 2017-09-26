def make_lazy(f, *args):
    return lambda: f(*args)
