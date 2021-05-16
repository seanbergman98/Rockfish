from abc import ABC, abstractmethod
from typing import List

from engine.board.board_utils import FIRST_ROW, SECOND_ROW, SEVENTH_ROW, EIGHTH_ROW, FIRST_COLUMN, SECOND_COLUMN, \
    SEVENTH_COLUMN, EIGHTH_COLUMN
from engine.board.move import Move
from engine.board.board import Board


class Piece(ABC):
    # TODO: Placeholder piece value for king since this piece is invaluable
    PIECE_VALUES = {
        'pawn': 100,
        'knight': 300,
        'bishop': 300,
        'rook': 500,
        'queen': 900,
        'king': 10_000
    }

    def __init__(self, piece_type, color, position, is_first_move):
        self.piece_type = piece_type
        self.color = color
        self.position = position
        self.is_first_move = is_first_move

    def get_piece_type(self):
        return self.piece_type

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def get_piece_value(self):
        return Piece.PIECE_VALUES[self.piece_type]

    def is_first_move(self):
        return self.is_first_move

    def is_pawn(self):
        if self.piece_type == 'pawn':
            return True
        else:
            return False

    def is_rook(self):
        if self.piece_type == 'rook':
            return True
        else:
            return False

    def is_knight(self):
        if self.piece_type == 'knight':
            return True
        else:
            return False

    def is_bishop(self):
        if self.piece_type == 'bishop':
            return True
        else:
            return False

    def is_queen(self):
        if self.piece_type == 'queen':
            return True
        else:
            return False

    def is_king(self):
        if self.piece_type == 'king':
            return True
        else:
            return False

    def is_in_first_row(self):
        return True if FIRST_ROW[self.position] else False

    def is_in_second_row(self):
        return True if SECOND_ROW[self.position] else False

    def is_in_seventh_row(self):
        return True if SEVENTH_ROW[self.position] else False

    def is_in_eighth_row(self):
        return True if EIGHTH_ROW[self.position] else False

    def is_in_first_column(self):
        return True if FIRST_COLUMN[self.position] else False

    def is_in_second_column(self):
        return True if SECOND_COLUMN[self.position] else False

    def is_in_seventh_column(self):
        return True if SEVENTH_COLUMN[self.position] else False

    def is_in_eighth_column(self):
        return True if EIGHTH_COLUMN[self.position] else False

    @abstractmethod
    def calculate_legal_moves(self, board: Board) -> List[Move]:
        pass
