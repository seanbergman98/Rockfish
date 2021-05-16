from abc import ABC, abstractmethod

from engine.pieces.piece import Piece


class Tile(ABC):

    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position

    @abstractmethod
    def get_piece(self):
        pass

    @abstractmethod
    def is_tile_occupied(self):
        pass


class EmptyTile(Tile):

    def __init__(self, position):
        super().__init__(position)

    def get_piece(self):
        return None

    def is_tile_occupied(self):
        return False


class OccupiedTile(Tile):

    def __init__(self, position, piece):
        super().__init__(position)
        self.piece = piece

    def get_piece(self) -> Piece:
        return self.piece

    def is_tile_occupied(self):
        return True
