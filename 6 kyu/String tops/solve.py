def tops(msg):
    result, i, offset = '', 1, 5
    while i < len(msg):
        result += msg[i]
        i += offset
        offset += 4
    return result[::-1]
