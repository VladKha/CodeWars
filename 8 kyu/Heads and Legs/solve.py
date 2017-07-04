def animals(heads, legs):
    cows = (legs - heads * 2) / 2
    chickens = heads - cows
    if heads < 0 or legs < 0 or chickens * cows < 0 or chickens % 1 != 0 or cows % 1 != 0:
        return 'No solutions'
    return chickens, cows
