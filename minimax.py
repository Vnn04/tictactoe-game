import math
from const import *
from board import Board as B

class MinimaxRoot:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.game_state = B().board_check()

    def evaluate(self, player):
        player_count = sum(row.count(player) for row in self.board)
        opponent_count = sum(row.count(-player) for row in self.board)

        return player_count - opponent_count
    
    def get_empty_cells(self):
        empty_cells = []
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if self.board[i][j] == 0:
                    empty_cells.append((i, j))
        
        return empty_cells
    
    def minimax(self, depth, maximizing_player, player):
        if depth == 0 or not (self.game_state):
            return self.evaluate(player)
        
        if maximizing_player:
            max_eval = -math.inf
            empty_cells = self.get_empty_cells()
            
            for cell in empty_cells:
                i, j = cell

                eval = self.minimax(depth - 1, False, player)
                self.board[i][j] = 0
                max_eval = max(max_eval, eval)
            return max_eval
        
        else:
            min_eval = math.inf
            empty_cells = self.get_empty_cells()

            for cell in empty_cells:
                i, j = cell
                self.board[i][j] = -player

                eval = self.minimax(depth - 1, True, player)
                self.board[i][j] = 0
                min_eval = min(min_eval, eval)

            return min_eval
        
    def best_move(self):
        best_eval = -math.inf
        best_move = None
        empty_cells = self.get_empty_cells()

        for cell in empty_cells:
            i, j = cell
            self.board[i][j] = self.player
            eval = self.minimax(5, False, self.player)
            self.board[i][j] = 0
            if eval > best_eval:
                best_eval = eval
                best_move = (i, j)
        return best_move