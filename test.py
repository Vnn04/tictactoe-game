import pygame
import math
from const import *

class Board:
    def __init__(self):
        self.vertical_line = []
        self.horizontal_line = []
        self.board_check = [[0 for j in range(ROWS)] for i in range(COLS)]

        for i in range(COLS):
            self.vertical_line.append(COLS * i)
        self.vertical_line.append(WIDTH)

        for j in range(ROWS):
            self.horizontal_line.append(ROWS * j)
        self.horizontal_line.append(HEIGHT)

    def draw(self, screen):
        for x in self.vertical_line:
            pygame.draw.line(screen, INDIANRED, (x, 0), (x, HEIGHT), 1)

        for y in self.horizontal_line:
            pygame.draw.line(screen, INDIANRED, (0, y), (WIDTH, y), 1)

    def click(self, pos, screen, player):
        if 0 <= pos[0] <= 900 and 0 <= pos[1] <= 900:
            x, y = pos[0]//ROWS, pos[1]//COLS
            if self.board_check[x][y] != 0:
                return False
            if player == 1:
                self.board_check[x][y] = 1
                pygame.draw.line(screen, YELLOW, (x * ROWS, y * COLS),
                                 (x * ROWS + WIDTH/ROWS, y * COLS + HEIGHT/COLS), 2)
                pygame.draw.line(screen, YELLOW, (x * ROWS + WIDTH/ROWS,
                                 y * COLS), (x * ROWS, y * COLS + HEIGHT/COLS), 2)
            elif player == -1:
                self.board_check[x][y] = -1
                pygame.draw.circle(screen, YELLOW, (x * ROWS + (WIDTH/ROWS)/2,
                                   y * COLS + (HEIGHT/COLS)/2), (WIDTH/ROWS)/2 - 2, 2)
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

    def check_five_in_a_row(self):
        rows = len(self.board_check)
        cols = len(self.board_check[0])

        for i in range(rows):
            for j in range(cols-4):
                subarray = self.board_check[i][j:j+5] 
                if self.check(subarray):
                    return True
                
        for i in range(rows - 4):
            for j in range(cols):
                subarray = [self.board_check[i+k][j] for k in range(5)]
                if self.check(subarray):
                    return True
                
        for i in range(rows - 4):
            for j in range(cols - 4):
                subarray = [self.board_check[i+k][j+k] for k in range(5)]
                if self.check(subarray):
                    return True
                
        for i in range(rows - 4):
            for j in range(4, cols):
                subarray = [self.board_check[i+k][j-k] for k in range(5)]
                if self.check(subarray):
                    return True
        
        return False


def minimax(board, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or board.check_five_in_a_row():
        return None, evaluate(board)

    if is_maximizing_player:
        best_score = -math.inf
        best_move = None
        for move in get_possible_moves(board):
            new_board = get_new_board(board, move, 1)
            _, new_score = minimax(new_board, depth-1, alpha, beta, False)
            if new_score > best_score:
                best_score = new_score
                best_move = move
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_move, best_score
    else:
        best_score = math.inf
        best_move = None
        for move in get_possible_moves(board):
            new_board = get_new_board(board, move, -1)
            _, new_score = minimax(new_board, depth-1, alpha, beta, True)
            if new_score < best_score:
                best_score = new_score
                best_move = move
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_move, best_score

def evaluate(board):
    if board.check_five_in_a_row():
        return math.inf if player == 1 else -math.inf
    else:
        return 0

def get_possible_moves(board):
    moves = []
    for i in range(COLS):
        for j in range(ROWS):
            if board.board_check[i][j] == 0:
                moves.append((i, j))
    return moves

def get_new_board(board, move, player):
    new_board = Board()
    new_board.board_check = [row[:] for row in board.board_check]
    new_board.board_check[move[0]][move[1]] = player
    return new_board

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Caro Game")
    board = Board()
    running = True
    player = 1
    depth = 4

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if player == 1:
                    pos = pygame.mouse.get_pos()
                    if board.click(pos, screen, player):
                        player = -1
                elif player == -1:
                    move, score = minimax(board, depth, -math.inf, math.inf, True)
                    board.click((move[0]*ROWS+ROWS/2, move[1]*COLS+COLS/2), screen, player)
                    player = 1

        board.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()