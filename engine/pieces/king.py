from engine.pieces.piece import Piece


class King(Piece):
    def __init__(self, color, position, is_first_move):
        super().__init__('king', color, position, is_first_move)
