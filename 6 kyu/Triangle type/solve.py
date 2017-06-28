def triangle_type(a, b, c):
    x, y, z = sorted([a, b, c])
    if z >= x + y:
        return 0
    if z * z == x * x + y * y:
        return 2
    return 1 if z * z < x * x + y * y else 3
