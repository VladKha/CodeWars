def get_derivative(s):
    if 'x' not in s:
        return '0'
    a = int(s.split('x')[0])
    b = 1
    parts = s.split('^')
    if len(parts) > 1:
        b = int(parts[1])
    if b == 2:
        return str(a * b) + 'x'
    elif b == 1:
        return str(a * b)
    return str(a * b) + 'x^' + str(b-1)
