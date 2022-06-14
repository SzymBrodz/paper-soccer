import pygame

from Players.Human import Human
from Players.MiniMax import MiniMax


class Game:
    board = None
    player1 = None
    player2 = None
    turn = True

    def __init__(self, board):
        self.board = board
        self.player1 = Human(self.board, True)
        self.player2 = MiniMax(self.board, False)

    def handle_moves(self):
        if self.turn:
            print("Player 1 turn!")
            if self.player1.make_move():
                self.turn = not self.turn
        else:
            print("Player 2 turn!")
            if self.player2.make_move():
                self.turn = not self.turn
        winner = self.board.check_winner(self.turn)
        if winner is not None:
            print(winner, " wins!")
            pygame.quit()
            quit()
