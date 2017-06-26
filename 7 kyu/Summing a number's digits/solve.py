def sumDigits(n):
    return sum(int(i) for i in str(abs(n)))
