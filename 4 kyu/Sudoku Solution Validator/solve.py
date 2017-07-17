def validSolution(board):
    a = {i for i in range(1, 10)}

    # check rows
    for row in board:
        if set(row) != a:
            return False

    # check cols
    for j in range(len(board[0])):
        col = [board[i][j] for i in range(len(board))]
        if set(col) != a:
            return False

    # check squares
    for left_shift in range(0, 9, 3):
        for down_shift in range(0, 9, 3):
            square = set(
                [board[i][j] for i in range(left_shift, 3+left_shift) for j in range(down_shift, 3 + down_shift)]
            )
            if set(square) != a:
                return False

    return True
