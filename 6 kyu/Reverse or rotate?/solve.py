def revrot(s, size):
    if size <= 0 or not s or size > len(s):
        return ''

    result = ''
    for i in range(0, len(s), size):
        chunk = s[i:i+size]
        if len(chunk) != size:
            break

        if sum(int(digit)**3 for digit in chunk) % 2 == 0:
            result += chunk[::-1]
        else:
            result += chunk[1:] + chunk[:1]
    return result
