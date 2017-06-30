def cyclops(n):
    binary = bin(n)[2:]
    mid = len(binary) // 2
    return binary[:mid] == binary[mid + 1:] and binary[mid] == '0'
