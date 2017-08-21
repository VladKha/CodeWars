def score_throws(radii):
    result = 0
    all_less_5 = True
    for r in radii:
        if r > 10:
            all_less_5 = False
        elif r < 5:
            result += 10
        else:
            result += 5
            all_less_5 = False
    if radii and all_less_5:
        result += 100
    return result
