import numpy as np

from const import *

class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0