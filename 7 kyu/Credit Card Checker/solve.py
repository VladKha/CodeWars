def valid_card(card):
    digits = list(map(int, card.replace(' ', '')))
    for i in range(0, len(digits), 2):
        value = digits[i] * 2
        if value > 9:
            value -= 9
        digits[i] = value
    return sum(digits) % 10 == 0
