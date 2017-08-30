def dating_range(age):
    if age <= 14:
        min_age = age - 0.1 * age
        max_age = age + 0.1 * age
    else:
        min_age = age / 2 + 7
        max_age = (age - 7) * 2
    return '{:.0f}-{:.0f}'.format(int(min_age), int(max_age))
