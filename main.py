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

    def mainloop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # draw board game
                self.board.draw(self.screen)
            
            pygame.display.update()

main = Main()
main.mainloop() 