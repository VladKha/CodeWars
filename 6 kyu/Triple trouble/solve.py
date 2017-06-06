def triple_double(num1, num2):
    a, b = str(num1), str(num2)
    for i in '0123456789':
        if i * 3 in a and i * 2 in b:
            return 1
    return 0
