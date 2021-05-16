from engine.pieces.piece import Piece
from engine.board.move import Move, AttackingMove
from engine.board.board_utils import FIRST_ROW, SECOND_ROW, SEVENTH_ROW, EIGHTH_ROW, FIRST_COLUMN, SECOND_COLUMN, \
    SEVENTH_COLUMN, EIGHTH_COLUMN


class Knight(Piece):
    CANDIDATE_MOVE_OFFSETS = [-17, -15, -10, -6, 6, 10, 15, 17]

    def __init__(self, color, position, is_first_move):
        super().__init__('knight', color, position, is_first_move)

    def calculate_legal_moves(self, board):
        legal_moves = []

        for offset in Knight.CANDIDATE_MOVE_OFFSETS:
            if Knight._is_first_column_exclusion(self.position, offset) or \
                    Knight._is_second_column_exclusion(self.position, offset) or \
                    Knight._is_seventh_column_exclusion(self.position, offset) or \
                    Knight._is_eighth_column_exclusion(self.position, offset) or \
                    Knight._is_first_row_exclusion(self.position, offset) or \
                    Knight._is_second_row_exclusion(self.position, offset) or \
                    Knight._is_seventh_row_exclusion(self.position, offset) or \
                    Knight._is_eighth_row_exclusion(self.position, offset):
                continue

            destination = self.position + offset
            destination_tile = board.get_tile(destination)
            if not destination_tile.is_tile_occupied():
                candidate_move = Move(board, self, destination)
            elif destination_tile.is_tile_occupied() and destination_tile.get_piece().get_color() != self.color:
                candidate_move = AttackingMove(board, self, destination, destination_tile.get_piece())
            else:
                candidate_move = None

            if candidate_move is not None:
                if not candidate_move.execute().leaves_player_in_check():
                    legal_moves.append(candidate_move)

    @staticmethod
    def _is_first_column_exclusion(position, offset):
        if FIRST_COLUMN[position]:
            if offset in [-17, -10, 6, 15]:
                return True
        return False

    @staticmethod
    def _is_second_column_exclusion(position, offset):
        if SECOND_COLUMN[position]:
            if offset in [-10, 6]:
                return True
        return False

    @staticmethod
    def _is_seventh_column_exclusion(position, offset):
        if SEVENTH_COLUMN[position]:
            if offset in [-6, 10]:
                return True
        return False

    @staticmethod
    def _is_eighth_column_exclusion(position, offset):
        if EIGHTH_COLUMN[position]:
            if offset in [-15, -6, 10, 17]:
                return True
        return False

    @staticmethod
    def _is_first_row_exclusion(position, offset):
        if FIRST_ROW[position]:
            if offset in [-17, -15, -10, -6]:
                return True
        return False

    @staticmethod
    def _is_second_row_exclusion(position, offset):
        if SECOND_ROW[position]:
            if offset in [-17, -15]:
                return True
        return False

    @staticmethod
    def _is_seventh_row_exclusion(position, offset):
        if SEVENTH_ROW[position]:
            if offset in [15, 17]:
                return True
        return False

    @staticmethod
    def _is_eighth_row_exclusion(position, offset):
        if EIGHTH_ROW[position]:
            if offset in [6, 10, 15, 17]:
                return True
        return False
