def calculator(x, y, op):
    if str(op) in '+-*/':
        return eval('{}{}{}'.format(x, op, y))
    return "unknown value"
