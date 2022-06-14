from abc import ABC, abstractmethod


class Player(ABC):
    board = None
    is_player_one = None

    def __init__(self, board, is_player_one):
        self.board = board
        self.is_player_one = is_player_one

    def make_move(self):
        direction = self.next_move()
        is_legal = self.board.points[self.board.ball_pos[0]][self.board.ball_pos[1]] & direction
        direction ^= 0b111111111
        if is_legal:
            if self.board.make_move(direction):
                return False
            else:
                return True
        else:
            print("not a valid move")
            return False

    @abstractmethod
    def next_move(self):
        pass
