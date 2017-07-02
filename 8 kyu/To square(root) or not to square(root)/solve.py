def square_or_square_root(arr):
    return [i * i if i ** 0.5 % 1 else i ** 0.5 for i in arr]
