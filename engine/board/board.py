from engine.board.board_utils import NUM_TILES, NUM_TILES_PER_ROW
from engine.board.tile import Tile, EmptyTile, OccupiedTile
from engine.pieces.bishop import Bishop
from engine.pieces.king import King
from engine.pieces.knight import Knight
from engine.pieces.pawn import Pawn
from engine.pieces.piece import Piece
from engine.pieces.queen import Queen
from engine.pieces.rook import Rook

import engine.board.move as mv


class Board:

    def __init__(self):
        self.board_tiles = [None] * NUM_TILES

    def get_active_pieces(self):
        return self.white_pieces if self.color_to_move == 'white' else self.black_pieces

    def get_opponent_pieces(self):
        return self.white_pieces if self.color_to_move == 'black' else self.black_pieces

    def get_legal_moves(self, piece):
        legal_moves = []

        if piece.is_pawn():
            pass
        elif piece.is_rook():
            pass
        elif piece.is_knight():
            move_offsets = Knight.CANDIDATE_MOVE_OFFSETS.copy()

            if self.is_in_first_column():
                move_offsets.remove(-10)
                move_offsets.remove(-17)
                move_offsets.remove(6)
                move_offsets.remove(15)
            elif self.is_in_second_column():
                move_offsets.remove(-10)
                move_offsets.remove(6)
            elif self.is_in_seventh_column():
                move_offsets.remove(-6)
                move_offsets.remove(10)
            elif self.is_in_eighth_column():
                move_offsets.remove(-15)
                move_offsets.remove(-6)
                move_offsets.remove(10)
                move_offsets.remove(17)

            if self.is_in_first_row():
                move_offsets.remove(-17)
                move_offsets.remove(-15)
                move_offsets.remove(-10)
                move_offsets.remove(-6)
            elif self.is_in_second_row():
                move_offsets.remove(-17)
                move_offsets.remove(-15)
            elif self.is_in_seventh_row():
                move_offsets.remove(15)
                move_offsets.remove(17)
            elif self.is_in_eighth_row():
                move_offsets.remove(6)
                move_offsets.remove(10)
                move_offsets.remove(15)
                move_offsets.remove(17)

            moves = []
            destinations = map(lambda x: piece.get_position() + x, move_offsets)

            #Create the moves
            for destination in destinations:
                destination_tile = self.get_tile(destination)
                if destination_tile.is_tile_occupied():
                    attacked_piece = destination_tile.get_piece()
                    move = mv.AttackingMove(self, piece, destination, attacked_piece)
                else:
                    move = mv.Move(self, piece, destination)
                moves.append(move)

        elif piece.is_bishop():
            pass
        elif piece.is_queen():
            pass
        elif piece.is_king():
            pass

        for move in moves:
            resulting_board = move.execute()
            if not resulting_board.leaves_player_in_check():
                legal_moves.append(move)

        return legal_moves


    def get_all_legal_moves(self):
        all_legal_moves = []
        for piece in self.get_active_pieces():
            for move in self.get_legal_moves(piece):
                all_legal_moves.append(move)
        return all_legal_moves

    def get_all_opponent_legal_moves(self):
        opponent_legal_moves = []
        for piece in self.get_opponent_pieces():
            for move in self.get_legal_moves(piece):
                opponent_legal_moves.append(move)
        return opponent_legal_moves

    def is_in_check(self):
        opponent_attacking_moves = filter(lambda x: x.is_attacking_move(), self.get_all_opponent_legal_moves)
        opponent_king_attacks = filter(lambda x: x.get_attacked_piece() == 'king', opponent_attacking_moves)

        if not opponent_king_attacks:
            return False
        else:
            True

    def is_in_checkmate(self):
        if self.is_in_check():
            if self.get_all_legal_moves():
                return True
        return False

    def leaves_player_in_check(self):
        attacking_moves = filter(lambda x: x.is_attacking_move(), self.get_all_legal_moves())
        king_attacks = filter(lambda x: x.get_attacked_piece() == 'king', attacking_moves)

        if not king_attacks:
            return False
        else:
            return True

    def get_tile(self, position):
        return self.board_tiles[position]

    @staticmethod
    def create_starting_board():
        board = Board()
        board.color_to_move = 'white'
        board.en_passant_pawn = None
        board.board_tiles[0] = OccupiedTile(0, Rook('white', 0, True))
        board.board_tiles[1] = OccupiedTile(1, Knight('white', 1, True))
        board.board_tiles[2] = OccupiedTile(2, Bishop('white', 2, True))
        board.board_tiles[3] = OccupiedTile(3, Queen('white', 3, True))
        board.board_tiles[4] = OccupiedTile(4, King('white', 4, True))
        board.board_tiles[5] = OccupiedTile(5, Bishop('white', 5, True))
        board.board_tiles[6] = OccupiedTile(6, Knight('white', 6, True))
        board.board_tiles[7] = OccupiedTile(7, Rook('white', 7, True))
        for position in range(8, 16):
            board.board_tiles[position] = OccupiedTile(position, Pawn('white', position, True))
        for position in range(16, 48):
            board.board_tiles[position] = EmptyTile(position)
        for position in range(48, 56):
            board.board_tiles[position] = OccupiedTile(position, Pawn('black', position, True))
        board.board_tiles[56] = OccupiedTile(56, Rook('black', 56, True))
        board.board_tiles[57] = OccupiedTile(57, Knight('black', 57, True))
        board.board_tiles[58] = OccupiedTile(58, Bishop('black', 58, True))
        board.board_tiles[59] = OccupiedTile(59, Queen('black', 59, True))
        board.board_tiles[60] = OccupiedTile(60, King('black', 60, True))
        board.board_tiles[61] = OccupiedTile(61, Bishop('black', 61, True))
        board.board_tiles[62] = OccupiedTile(62, Knight('black', 62, True))
        board.board_tiles[63] = OccupiedTile(63, Rook('black', 63, True))

        occupied_tiles = filter(lambda x: x.is_tile_occupied(), board.board_tiles)
        all_pieces = map(lambda x: x.get_piece(), occupied_tiles)
        white_pieces = filter(lambda x: x.get_color() == 'white', all_pieces)
        black_pieces = filter(lambda x: x.get_color() == 'black', all_pieces)
        board.white_pieces = white_pieces
        board.black_pieces = black_pieces

        return board


class Builder:

    def __init__(self):
        self.board = Board()

    def set_tile(self, position, tile):
        self.board.board_tiles[position] = tile

    def set_color_to_move(self, color):
        self.board.color_to_move = color

    def set_en_passant_pawn(self, pawn):
        self.board.en_passant_pawn = pawn

    def build(self):
        occupied_tiles = filter(lambda x: x.is_tile_occupied(), self.board.board_tiles)
        all_pieces = map(lambda x: x.get_piece(), occupied_tiles)
        white_pieces = filter(lambda x: x.get_color() == 'white', all_pieces)
        black_pieces = filter(lambda x: x.get_color() == 'black', all_pieces)
        self.board.white_pieces = white_pieces
        self.board.black_pieces = black_pieces
        return self.board



