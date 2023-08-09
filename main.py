import sys
import pygame
import time
import threading

from const import *
from game import Game
from ai import AI
from menu import Menu

# pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic tac toe')
screen.fill(BG_COLOR)

def main():

    menu = Menu(screen)
    menu.show()
    
    game = Game(screen)
    board = game.board
    ai = game.ai

    # main loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if board.empty_sqr(row, col) and game.can_choose:
                    game.make_move(row, col)

                    if game.is_over():
                        game.running = False
            
            if event.type == pygame.KEYDOWN:
                # 0-random ai
                if event.key == pygame.K_0:
                    ai.level = 0
                # 1-random ai
                elif event.key == pygame.K_1:
                    ai.level = 1
                # r-reset game
                elif event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai


        if game.player == ai.player and game.running:
            # update the screen
            pygame.display.update()

            # ai methods
            row, col = ai.eval(board)
            game.make_move(row, col)


            if game.is_over():
                game.show_win()
                game.running = False

        pygame.display.update()

main()