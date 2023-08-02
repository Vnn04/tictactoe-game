import pygame

from const import *

class Board:
    def __init__(self):
        self.vertical_line = []
        self.horizontal_line = []
        # init 2D array
        self.board_check = [[0 for j in range(30)] for i in range(30)]

        # get all vertical line position in the board
        for i in range(COLS):
            self.vertical_line.append(COLS * i)
        self.vertical_line.append(WIDTH)

        # get all horizontal line position in the board
        for j in range(ROWS):
            self.horizontal_line.append(ROWS * j)
        self.horizontal_line.append(HEIGHT)

    def draw(self, screen):
        # draw vertical lines
        for x in self.vertical_line:
            pygame.draw.line(screen, INDIANRED, (x, 0), (x, HEIGHT), 1)

        # draw horizontal lines
        for y in self.horizontal_line:
            pygame.draw.line(screen, INDIANRED, (0, y), (WIDTH, y), 1)

    def in_check(self):
        pass

    def click(self, pos, screen, player):
        if 0 <= pos[0] <= 900 and 0 <= pos[1] <= 900:
            x, y = pos[0]//COLS, pos[1]//ROWS
            if player == 1 and self.board_check[x][y] == 0:
                self.board_check[y][x] = 1000
                pygame.draw.line(screen, YELLOW, (x * COLS, y * ROWS),
                                 (x * COLS + WIDTH/COLS, y * ROWS + HEIGHT/ROWS), 2)
                pygame.draw.line(screen, YELLOW, (x * COLS + WIDTH/COLS,
                                 y * ROWS), (x * COLS, y * ROWS + HEIGHT/ROWS), 2)
            elif player == -1 and self.board_check[x][y] == 0:
                self.board_check[y][x] = -1000
                pygame.draw.circle(screen, YELLOW, (x * COLS + (WIDTH/COLS)/2,
                                   y * ROWS + (HEIGHT/ROWS)/2), (WIDTH/COLS)/2 - 2, 2)
            return True
        return False
    
    def show_board(self):
        print(self.board_check)