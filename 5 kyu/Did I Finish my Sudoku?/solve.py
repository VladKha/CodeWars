import numpy as np


def done_or_not(board):
    board = np.array(board)

    rows = [board[i, :] for i in range(9)]
    cols = [board[:, j] for j in range(9)]
    sqrs = [board[i:i + 3, j:j + 3].flatten() for i in [0, 3, 6] for j in [0, 3, 6]]

    for view in np.vstack((rows, cols, sqrs)):
        if len(np.unique(view)) != 9:
            return 'Try again!'

    return 'Finished!'
