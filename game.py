import pygame
import numpy as np

from const import *
from board import Board
from ai import AI

class Game:
    def __init__(self, surface):
        self.board = Board()
        self.ai = AI()
        self.show_lines(surface)
        self.player = 1
        self.running = True
        self.surface = surface
        self.can_choose = True

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def show_lines(self, surface):
        # BG 
        surface.fill(BG_COLOR)
        # vertical
        pygame.draw.line(surface, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(surface, LINE_COLOR, (SQSIZE * 2, 0), (SQSIZE * 2, HEIGHT), LINE_WIDTH)
        # horizontal
        pygame.draw.line(surface, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(surface, LINE_COLOR, (0, SQSIZE * 2), (WIDTH, SQSIZE * 2), LINE_WIDTH)

    def draw_fig(self, row, col):
        if self.player == 1:
            # draw cross
            # desc line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(self.surface, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

            # asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE-+ OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(self.surface, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

        elif self.player == -1:
            # draw circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(self.surface, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    def next_turn(self):
        self.player = -self.player

    def reset(self):
        self.__init__(self.surface)

    def is_over(self):
        return self.board.final_state(show=True) != 0 or self.board.is_full()
    
    def show_win(self):
        if self.is_over():
            pygame.draw.line(self.surface, self.board.color, self.board.iPos, self.board.fPos, LINE_WIDTH)
            self.can_choose = False