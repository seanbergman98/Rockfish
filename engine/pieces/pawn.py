from engine.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, color, position, is_first_move):
        super().__init__('pawn', color, position, is_first_move)
