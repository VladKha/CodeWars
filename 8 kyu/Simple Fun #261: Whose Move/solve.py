def whoseMove(lastPlayer, win):
    return lastPlayer if win else {'black': 'white', 'white': 'black'}[lastPlayer]
