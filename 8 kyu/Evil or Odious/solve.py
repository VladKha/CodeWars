def evil(n):
    return "It's Evil!" if bin(n)[2:].count('1') % 2 == 0 else "It's Odious!"
