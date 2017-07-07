def show_sequence(n):
    if n < 0:
        return '{}<0'.format(n)
    elif n == 0:
        return '0=0'
    return '+'.join(str(i) for i in range(n+1)) + ' = ' + str(n * (n + 1) // 2)
