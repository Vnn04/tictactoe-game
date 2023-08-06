import pygame
import sys

from const import *
from board import Board

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Checkerboard game")
        self.board = Board()
        self.player = 1 # 1 or -1

    def mainloop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    if self.board.click(self.pos, self.screen, self.player):
                        self.player = 1 if self.player == -1 else -1

                # draw board game
                self.board.draw(self.screen)
                if self.board.check_three_in_a_row():
                    print(True)
                    sys.exit()            
            pygame.display.update()

main = Main()
main.mainloop() 