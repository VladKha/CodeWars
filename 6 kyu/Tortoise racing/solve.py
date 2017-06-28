def race(v1, v2, g):
    if v1 >= v2:
        return None
    t = g * 60 * 60 / (v2 - v1)
    return [t // 3600, t % 3600 // 60, int(t % 60)]
