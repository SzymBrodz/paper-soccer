from copy import deepcopy, copy
import time
import pygame.event
from Player import Player

class MiniMax(Player):
    move_queue = []

    def __init__(self, board, is_player_one):
        super().__init__(board, is_player_one)

    # funkcja heurystyczna
    def heur(self, game_board):
        point_cap = (game_board.height-2)*5
        for i in range(1, game_board.height-1):
            if game_board.ball_pos[0] == i:
                if self.is_player_one:
                    reward = point_cap-i*5
                    return reward
                else:
                    reward = i*5
                    return reward





    def minimax(self, board, depth, is_max_player, alfa=-2000, beta=2000):
        if board.check_if_won(self.is_player_one):
            return 100, None
        elif board.check_if_won(not self.is_player_one):
            return -100, None

        if depth == 0:
            return self.heur(board), None

        if is_max_player:
            max_eval = -3000
            best_move = None
            possible_moves = board.get_possible_moves(this_path=[])
            for move in possible_moves:
                # print("sprawdziłem dla maxa ruch" + str(move))
                # wykonanie ruchu
                board_copy = deepcopy(board)
                for m in move:
                    m_r = m ^ 0b111111111
                    board_copy.make_move(m_r)

                eval, new_move = self.minimax(board_copy, depth - 1, False, alfa, beta)
                if eval > max_eval:
                    max_eval, best_move = eval, move
                alfa = max(alfa, eval)
                if beta <= alfa:
                    break
            return max_eval, best_move

        else:
            min_eval = 3000
            best_move = None
            possible_moves = board.get_possible_moves(this_path=[])
            for move in possible_moves:
                # print("sprawdziłem dla mina ruch" + str(move))
                # wykonanie ruchu
                board_copy = deepcopy(board)
                for m in move:
                    m_r = m ^ 0b111111111
                    board_copy.make_move(m_r)

                eval, new_move = self.minimax(board_copy, depth - 1, True, alfa, beta)
                if eval < min_eval:
                    min_eval, best_move = eval, move
                beta = min(alfa, eval)
                if beta <= alfa:
                    break

            return min_eval, best_move

    def next_move(self):
        if len(self.move_queue) == 0:
            tic = time.time()
            x, self.move_queue = self.minimax(self.board, 2, True)
            toc = time.time()
            print(str(toc - tic) + "s")

        move = self.move_queue[0]
        self.move_queue.pop(0)
        return move
