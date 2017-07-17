import numpy as np
from math import sqrt


class Sudoku:
    def __init__(self, board):
        self.data = board

    def is_valid(self):
        n = len(self.data)
        if type(self.data[0]) is not list:
            return False
        for row in self.data:
            if len(row) != n:
                return False
            for value in row:
                if type(value) != int:
                    return False

        size = int(sqrt(n))
        board = np.array(self.data)

        rows = [board[i, :] for i in range(n)]
        cols = [board[:, j] for j in range(n)]
        squares = [board[i:i + size, j:j + size].flatten() for i in range(0, n, size) for j in
                   range(0, n, size)]

        a = set([i for i in range(1, n + 1)])
        for view in np.vstack((rows, cols, squares)):
            if set(view.tolist()) != a:
                return False

        return True
