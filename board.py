import pygame

from const import *

class Board:
    def __init__(self):
        self.vertical_line = []
        self.horizontal_line = []
        # init 2D array
        self.board_check = [[0 for j in range(ROWS)] for i in range(COLS)]

        self.col_size = WIDTH // COLS
        self.row_size = HEIGHT // ROWS

        # get all vertical line position in the board
        for i in range(HEIGHT):
            self.vertical_line.append(self.row_size * i)
        self.vertical_line.append(WIDTH)

        # get all horizontal line position in the board
        for j in range(WIDTH):
            self.horizontal_line.append(self.col_size * j)
        self.horizontal_line.append(HEIGHT)

    def draw(self, screen):
        # draw vertical lines
        for x in self.vertical_line:
            pygame.draw.line(screen, INDIANRED, (x, 0), (x, HEIGHT), 1)

        # draw horizontal lines
        for y in self.horizontal_line:
            pygame.draw.line(screen, INDIANRED, (0, y), (WIDTH, y), 1)

    def click(self, pos, screen, player):
        if 0 <= pos[0] <= 900 and 0 <= pos[1] <= 900:
            x, y = pos[0]//self.col_size, pos[1]//self.row_size
            if self.board_check[x][y] != 0:
                return False
            if player == 1:
                self.board_check[x][y] = 1
                pygame.draw.line(screen, YELLOW, (x * self.col_size, y * self.row_size),
                                 (x * self.col_size + self.col_size, y * self.row_size + self.row_size), 2)
                pygame.draw.line(screen, YELLOW, (x * self.col_size + self.col_size,
                                 y * self.row_size), (x * self.col_size, y * self.row_size + self.row_size), 2)
            elif player == -1:
                self.board_check[x][y] = -1
                pygame.draw.circle(screen, YELLOW, (x * self.col_size + (self.col_size)/2,
                                   y * self.row_size + (self.row_size)/2), (self.col_size)/2 - 2, 2)
            return True
        return False
    
    def check(self, array):
        test = array[0]
        if test == 0:
            return False
        for i in range(1, len(array)):
            if array[i] != test:
                return False
        return True

    # def check_five_in_a_row(self):
    #     rows = len(self.board_check)
    #     cols = len(self.board_check[0])

    #     for i in range(rows):
    #         for j in range(cols-4):
    #             subarray = self.board_check[i][j:j+5] 
    #             if self.check(subarray):
    #                 return True
                
    #     for i in range(rows - 4):
    #         for j in range(cols):
    #             subarray = [self.board_check[i+k][j] for k in range(5)]
    #             if self.check(subarray):
    #                 return True
                
    #     for i in range(rows - 4):
    #         for j in range(cols - 4):
    #             subarray = [self.board_check[i+k][j+k] for k in range(5)]
    #             if self.check(subarray):
    #                 return True
                
    #     for i in range(rows - 4):
    #         for j in range(4, cols):
    #             subarray = [self.board_check[i+k][j-k] for k in range(5)]
    #             if self.check(subarray):
    #                 return True
        
    #     return False

    def check_three_in_a_row(self):
        rows = len(self.board_check)
        cols = len(self.board_check[0])

        for i in range(rows):
            for j in range(cols-2):
                subarray = self.board_check[i][j:j+3] 
                if self.check(subarray):
                    return True
                
        for i in range(rows - 2):
            for j in range(cols):
                subarray = [self.board_check[i+k][j] for k in range(3)]
                if self.check(subarray):
                    return True
                
        for i in range(rows - 2):
            for j in range(cols - 2):
                subarray = [self.board_check[i+k][j+k] for k in range(3)]
                if self.check(subarray):
                    return True
                
        for i in range(rows - 2):
            for j in range(2, cols):
                subarray = [self.board_check[i+k][j-k] for k in range(3)]
                if self.check(subarray):
                    return True
        
        return False