import pygame

from const import *
from board import Board
from ai import AI

class Game:
    def __init__(self, surface):
        self.board = Board()
        self.ai = AI()
        self.show_lines(surface)
        self.player = 1
        self.gamemode = 'ai' # pvp or ai
        self.running = True
        self.surface = surface

    def show_lines(self, surface):
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