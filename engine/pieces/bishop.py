from engine.pieces.piece import Piece
from engine.board.board_utils import FIRST_ROW, EIGHTH_ROW, FIRST_COLUMN, EIGHTH_COLUMN
from engine.board.move import Move, AttackingMove


class Bishop(Piece):
    CANDIDATE_MOVE_VECTORS = [-9, -7, 7, 9]

    def __init__(self, color, position, is_first_move):
        super().__init__('bishop', color, position, is_first_move)

    def calculate_legal_moves(self, board):
        legal_moves = []

        for vector in Bishop.CANDIDATE_MOVE_VECTORS:
            curr_position = self.position

            # So long as we haven't haven't reached the edges of the board
            while not (Bishop._is_first_column_exclusion(curr_position, vector) or
                       Bishop._is_eighth_column_exclusion(curr_position, vector) or
                       Bishop._is_first_row_exclusion(curr_position, vector) or
                       Bishop._is_eighth_row_exclusion(curr_position, vector)):

                destination = curr_position + vector
                destination_tile = board.get_tile(destination)

                if destination_tile.is_tile_occupied():

                    # If the piece on the destination tile is the same color as the moved piece, we can make no more
                    # moves in this direction
                    if destination_tile.get_piece().get_color() == self.color:
                        break
                    # Otherwise the piece must be of the opposite color, and we may make exactly one more move
                    else:
                        candidate_move = AttackingMove(board, self, destination, destination_tile.get_piece())
                        if not candidate_move.execute().leaves_player_in_check():
                            legal_moves.append(candidate_move)
                        break
                else:
                    candidate_move = Move(board, self, destination)
                    if not candidate_move.execute().leaves_player_in_check():
                        legal_moves.append(candidate_move)

                curr_position += vector

        return legal_moves

    @staticmethod
    def _is_first_column_exclusion(position, offset):
        if FIRST_COLUMN[position]:
            if offset in [-9, 7]:
                return True
        return False

    @staticmethod
    def _is_eighth_column_exclusion(position, offset):
        if EIGHTH_COLUMN[position]:
            if offset in [-7, 9]:
                return True
        return False

    @staticmethod
    def _is_first_row_exclusion(position, offset):
        if FIRST_ROW[position]:
            if offset in [-7, -9]:
                return True
        return False

    @staticmethod
    def _is_eighth_row_exclusion(position, offset):
        if EIGHTH_ROW[position]:
            if offset in [7, 9]:
                return True
        return False
