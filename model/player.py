from .piece import Piece

class Player:
    def __init__(self, name, piece,ai=False,turn=False):
        self.name = name
        self.piece = piece
        self.ai=ai
        self.turn=turn
