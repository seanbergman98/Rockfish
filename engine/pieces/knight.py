from engine.pieces.piece import Piece


class Knight(Piece):
    CANDIDATE_MOVE_OFFSETS = [-17, -15, -10, -6, 6, 10, 15, 17]

    def __init__(self, color, position, is_first_move):
        super().__init__('knight', color, position, is_first_move)

'''''''''
    def calculate_candidate_moves(self, board):
        candidate_moves = []
        candidate_move_offsets = Knight.CANDIDATE_MOVE_OFFSETS.copy()

        if self.__is_in_first_column():
            candidate_move_offsets.remove(-10)
            candidate_move_offsets.remove(-17)
            candidate_move_offsets.remove(6)
            candidate_move_offsets.remove(15)
        elif self.__is_in_second_column():
            candidate_move_offsets.remove(-10)
            candidate_move_offsets.remove(6)
        elif self.__is_in_seventh_column():
            candidate_move_offsets.remove(-6)
            candidate_move_offsets.remove(10)
        elif self.__is_in_eighth_column():
            candidate_move_offsets.remove(-15)
            candidate_move_offsets.remove(-6)
            candidate_move_offsets.remove(10)
            candidate_move_offsets.remove(17)

        if self.__is_in_first_row():
            candidate_move_offsets.remove(-17)
            candidate_move_offsets.remove(-15)
            candidate_move_offsets.remove(-10)
            candidate_move_offsets.remove(-6)
        elif self.__is_in_second_row():
            candidate_move_offsets.remove(-17)
            candidate_move_offsets.remove(-15)
        elif self.__is_in_seventh_row():
            candidate_move_offsets.remove(15)
            candidate_move_offsets.remove(17)
        elif self.__is_in_eighth_row():
            candidate_move_offsets.remove(6)
            candidate_move_offsets.remove(10)
            candidate_move_offsets.remove(15)
            candidate_move_offsets.remove(17)

        for vector in candidate_move_offsets:
            destination = self.position + vector
            destination_tile = board.get_tile(destination)
            if not destination_tile.is_tile_occupied():
                candidate_moves.append(Move(board, self, destination))
            elif destination_tile.is_tile_occupied() and destination_tile.get_piece().get_color() != self.color:
                candidate_moves.append(AttackingMove(board, self, destination, destination_tile.get_piece()))
'''''''''
