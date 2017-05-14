from collections import defaultdict


def check_diagonals(field):
    rows = len(field)
    cols = len(field[0])

    for r in range(rows - 1):
        for c in range(cols - 1):
            if field[r][c] == 1:
                if field[r + 1][c + 1] == 1:
                    return False
                if c != 0 and field[r + 1][c - 1] == 1:
                    return False

    return True


def check_sizes(field):
    rows = len(field)
    cols = len(field[0])

    counts = defaultdict(int)

    for r in range(rows):
        tmp = 0
        for c in range(cols):
            cell = field[r][c]

            if cell == 1:
                tmp += 1
            elif tmp == 1:
                if (r > 0 and field[r - 1][c - 1] == 1) or (r < rows - 1 and field[r + 1][c - 1]):
                    tmp = 0
                else:
                    counts[tmp] += 1
                    tmp = 0
            elif tmp >= 2:
                counts[tmp] += 1
                tmp = 0

    for c in range(cols):
        tmp = 0
        for r in range(rows):
            cell = field[r][c]

            if cell == 1:
                tmp += 1
            elif tmp == 1:
                if (c > 0 and field[r - 1][c - 1] == 1) or (c < cols - 1 and field[r - 1][c + 1]):
                    tmp = 0
                else:
                    counts[tmp] += 1
                    tmp = 0
            elif tmp >= 2:
                counts[tmp] += 1
                tmp = 0

    return len(counts) == 4 and counts[1] == 8 and counts[2] == 3 and counts[3] == 2 and counts[4] == 1


def validateBattlefield(field):
    tmp = check_sizes(field)
    print(tmp)
    return check_diagonals(field) and check_sizes(field)
