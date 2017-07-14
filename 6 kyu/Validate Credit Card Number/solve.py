def validate(n):
    i = 0
    result = 0
    while n:
        digit = n % 10
        n //= 10
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        result += digit
        i += 1
    return result % 10 == 0
