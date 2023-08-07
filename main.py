import pygame
import sys
from math import inf
from random import choice

from const import *
from board import Board

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Checkerboard game")
        self.board = Board()
        self.human = -1
        self.comp = +1
        self.player = self.human

    def evaluate(self):
        if self.wins(self.comp):
            score = +1
        elif self.wins(self.human):
            score = -1
        else:
            score = 0
        return score

    def wins(self, player):
        if self.board.check_three_in_a_row(player):
            return True
        return False
    
    def game_over(self):
        return self.wins(self.comp) or self.wins(self.human)
    
    def empty_cells(self):
        cells = []

        for x, row in enumerate(self.board.board_check):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells
    
    def valid_move(self, x, y):
        if [x, y] in self.empty_cells():
            return True
        return False
    
    def minimax(self, depth, player):
        if player == self.comp:
            best = [-1, -1, -inf]
        else:
            best = [-1, -1, +inf]

        if depth == 0 or self.game_over():
            score = self.evaluate()
            return [-1, -1, score]
        
        for cell in self.empty_cells():
            x, y = cell[0], cell[1]
            self.board.board_check[x][y] = player
            score = self.minimax(depth - 1, -player)
            self.board.board_check[x][y] = 0
            score[0], score[1] = x, y

            if player == self.comp:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score
            return best
        
    def ai_turn(self):
        depth = 9
        if depth == 0 or self.game_over():
            return 
        
        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = self.minimax(depth, self.comp)
            x, y = move[0], move[1]
        return (x, y)
            

    def mainloop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.player == self.human:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.pos = pygame.mouse.get_pos()
                        # if self.game_over():
                        #     print(True)
                        #     sys.exit()
                        if self.player == self.human:
                            self.board.player_move(self.pos, self.screen)
                            self.player = self.comp
                elif self.player == self.comp:
                    self.board.ai_move(self.ai_turn(), self.screen)
                    self.player = self.human
                

                # draw board game
                self.board.draw(self.screen)
                if self.board.check_three_in_a_row(self.player):
                    print(True)
                    sys.exit()            
            pygame.display.update()

main = Main()
main.mainloop() 