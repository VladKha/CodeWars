def knightVsKing(knightPosition, kingPosition):
    dx = abs(knightPosition[0] - kingPosition[0])
    dy = abs(ord(knightPosition[1]) - ord(kingPosition[1]))
    d = dx * dx + dy * dy

    if d == 5:
        return 'Knight'
    elif d <= 2:
        return 'King'
    else:
        return 'None'
