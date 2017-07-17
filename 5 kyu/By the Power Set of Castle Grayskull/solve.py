def power(s):
    power_set = [[]]
    for num in s:
        power_set += [x+[num] for x in power_set]
    return power_set
