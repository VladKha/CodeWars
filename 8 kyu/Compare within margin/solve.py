def close_compare(a, b, margin=0):
    if abs(a-b) <= margin:
        return 0
    return 1 if a > b else -1
