import numpy as np

from const import *

class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.mark_sqrs = 0
        self.iPos = 0
        self.fPos = 0
        self.color = None
        
    def final_state(self, show=False):
        '''
            @return 0 if there is not winner
            @return 1 if player 1 wins
            @return -1 if player -1 wins
        '''
        # vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    self.color = CIRC_COLOR if self.squares[0][col] == -1 else CROSS_COLOR
                    self.iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    self.fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                return self.squares[0][col]
        
        # horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    self.color = CIRC_COLOR if self.squares[0][col] == -1 else CROSS_COLOR
                    self.iPos = (20, row * SQSIZE + SQSIZE // 2)
                    self.fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                return self.squares[row][0]
        
        # desc diagonal
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                    self.color = CIRC_COLOR if self.squares[0][col] == -1 else CROSS_COLOR
                    self.iPos = (20, 20)
                    self.fPos = (WIDTH - 20, HEIGHT - 20)
            return self.squares[0][0]
        
        # asc diagonal
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            if show:
                    self.color = CIRC_COLOR if self.squares[0][col] == -1 else CROSS_COLOR
                    self.iPos = (20, HEIGHT - 20)
                    self.fPos = (WIDTH - 20, 20)
            return self.squares[0][2]
        # no winner
        return 0


    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.mark_sqrs += 1

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0
    
    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))
        return empty_sqrs
    
    def is_full(self):
        return self.mark_sqrs == 9
    
    def is_empty(self):
        return self.mark_sqrs == 0
    
    def winner(self):
        if self.final_state() != 0:
            return self.final_state()
        if self.is_full():
            return 0
        return None