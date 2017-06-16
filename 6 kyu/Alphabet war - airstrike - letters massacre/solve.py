def alphabet_war(fight):
    power = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}

    fight_new = '' if '*' in fight[0:2] else fight[0]
    for i in range(1, len(fight) - 1):
        if '*' not in fight[i-1:i+2]:
            fight_new += fight[i]
    fight_new += '' if '*' in fight[-2:] else fight[-1]

    r = sum(power[c] for c in fight_new if c in power)

    if r > 0:
        return "Left side wins!"
    elif r < 0:
        return "Right side wins!"
    return "Let's fight again!"
