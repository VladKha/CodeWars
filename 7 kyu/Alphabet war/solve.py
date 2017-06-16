def alphabet_war(fight):
    left_power = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_power = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left, right = 0, 0

    for ch in fight:
        if ch in left_power:
            left += left_power[ch]
        elif ch in right_power:
            right += right_power[ch]

    if left > right:
        return "Left side wins!"
    elif right > left:
        return "Right side wins!"
    return "Let's fight again!"
