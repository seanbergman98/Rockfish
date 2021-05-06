from engine.pieces.piece import Piece


class Bishop(Piece):
    CANDIDATE_MOVE_VECTORS = [-9, -7, 7, 9]

    def __init__(self, color, position, is_first_move):
        super().__init__('bishop', color, position, is_first_move)
