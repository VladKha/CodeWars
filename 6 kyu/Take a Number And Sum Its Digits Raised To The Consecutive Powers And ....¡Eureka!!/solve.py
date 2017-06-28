def sum_dig_pow(a, b):
    return [
        i for i in range(a, b+1) if i == sum(int(c) ** (j+1) for j,c in enumerate(str(i)))
    ]
