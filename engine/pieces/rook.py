from engine.pieces.piece import Piece


class Rook(Piece):
    def __init__(self, color, position, is_first_move):
        super().__init__('rook', color, position, is_first_move)
