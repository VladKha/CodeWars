def rgb(r, g, b):
    f = lambda x: min(255, max(x, 0))
    return '{:02X}{:02X}{:02X}'.format(f(r), f(g), f(b))
