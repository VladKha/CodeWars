def mineLocation(field):
    for (i, row) in enumerate(field):
        for (j, cell) in enumerate(row):
            if cell:
                return [i, j]
