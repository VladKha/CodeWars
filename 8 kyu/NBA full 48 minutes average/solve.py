def nba_extrap(ppg, mpg):
    return round(ppg * 48.0 / mpg, 1) if mpg > 0 else 0
