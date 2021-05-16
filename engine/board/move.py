from engine.board.board_utils import NUM_TILES, NUM_TILES_PER_ROW
from engine.board.tile import EmptyTile, OccupiedTile
from engine.board.board import Builder


class Move:

    # Note that the board we pass to our Move constructor is the board the move is happening on prior to completion
    def __init__(self, board, moved_piece, destination):
        self.board = board
        self.moved_piece = moved_piece
        self.destination = destination

    def get_moved_piece(self):
        return self.moved_piece

    def get_start(self):
        return self.moved_piece.get_position()

    def get_destination(self):
        return self.destination

    def get_highlight_tiles(self):
        highlight_tiles = [self.get_start(), self.get_destination()]
        return highlight_tiles

    def is_attacking_move(self):
        return False

    def execute(self):
        builder = Builder()

        if self.moved_piece.get_color() == 'white':
            builder.set_color_to_move('black')
        else:
            builder.set_color_to_move('white')

        builder.set_en_passant_pawn(None)

        for tile in self.board.board_tiles:
            builder.set_tile(tile.get_position(), tile)

        builder.set_tile(self.get_start(), EmptyTile(self.get_start()))

        # TODO: This is really bad form and needs to eventually be fixed
        new_piece = self.moved_piece
        new_piece.is_first_move = False
        new_piece.position = self.get_destination()
        builder.set_tile(self.get_destination(), OccupiedTile(self.get_destination(), new_piece))

        return builder.build()


class AttackingMove(Move):

    def __init__(self, board, moved_piece, destination, attacked_piece):
        super().__init__(board, moved_piece, destination)
        self.attacked_piece = attacked_piece

    def is_attacking_move(self):
        return True

    def get_attacked_piece(self):
        return self.attacked_piece


class PawnJump(Move):

    def execute(self):
        builder = Builder()

        if self.moved_piece.get_color() == 'white':
            builder.set_color_to_move('black')
        else:
            builder.set_color_to_move('white')

        for tile in self.board.board_tiles:
            builder.set_tile(tile.get_position(), tile)

        builder.set_tile(self.get_start(), EmptyTile(self.get_start()))

        # TODO: This is really bad form and needs to eventually be fixed
        new_pawn = self.moved_piece
        new_pawn.is_first_move = False
        new_pawn.position = self.get_destination()
        builder.set_tile(self.get_destination(), OccupiedTile(self.get_destination(), new_pawn))

        builder.set_en_passant_pawn(new_pawn)

        return builder.build()


class KingsideCastlingMove(Move):

    def __init__(self, board, moved_king, king_destination, moved_rook, rook_destination):
        self.board = board
        self.moved_king = moved_king
        self.king_destination = king_destination
        self.moved_rook = moved_rook
        self.rook_destination = rook_destination

    def get_king_start(self):
        return self.moved_king.get_position()

    def get_king_destination(self):
        return self.king_destination

    def get_rook_start(self):
        return self.moved_rook.get_position()

    def get_rook_destination(self):
        return self.rook_destination

    def execute(self):
        builder = Builder()

        if self.moved_king.get_color() == 'white':
            builder.set_color_to_move('black')
        else:
            builder.set_color_to_move('white')

        builder.set_en_passant_pawn(None)

        for tile in self.board.board_tiles:
            builder.set_tile(tile.get_position(), tile)

        # TODO: This is still really bad form
        builder.set_tile(self.get_king_start(), EmptyTile(self.get_king_start()))
        new_king = self.moved_king
        new_king.is_first_move = False
        new_king.position = self.get_king_destination()
        builder.set_tile(self.get_king_destination(), OccupiedTile(self.get_king_destination(), new_king))

        builder.set_tile(self.get_rook_start(), EmptyTile(self.get_rook_start()))
        new_rook = self.moved_rook
        new_rook.is_first_move = False
        new_rook.position = self.get_rook_destination()
        builder.set_tile(self.get_rook_destination(), OccupiedTile(self.get_rook_destination(), new_rook))

        return builder.build()

    def get_highlight_tiles(self):
        return [self.get_king_destination(), self.get_rook_destination()]


class QueensideCastlingMove(Move):

    def __init__(self, board, moved_king, king_destination, moved_rook, rook_destination):
        self.board = board
        self.moved_king = moved_king
        self.king_destination = king_destination
        self.moved_rook = moved_rook
        self.rook_destination = rook_destination

    def get_king_start(self):
        return self.moved_king.get_position()

    def get_king_destination(self):
        return self.king_destination

    def get_rook_start(self):
        return self.moved_rook.get_position()

    def get_rook_destination(self):
        return self.rook_destination

    def execute(self):
        builder = Builder()

        if self.moved_king.get_color() == 'white':
            builder.set_color_to_move('black')
        else:
            builder.set_color_to_move('white')

        builder.set_en_passant_pawn(None)

        for tile in self.board.board_tiles:
            builder.set_tile(tile.get_position(), tile)

        # TODO: This is still really bad form
        builder.set_tile(self.get_king_start(), EmptyTile(self.get_king_start()))
        new_king = self.moved_king
        new_king.is_first_move = False
        new_king.position = self.get_king_destination()
        builder.set_tile(self.get_king_destination(), OccupiedTile(self.get_king_destination(), new_king))

        builder.set_tile(self.get_rook_start(), EmptyTile(self.get_rook_start()))
        new_rook = self.moved_rook
        new_rook.is_first_move = False
        new_rook.position = self.get_rook_destination()
        builder.set_tile(self.get_rook_destination(), OccupiedTile(self.get_rook_destination(), new_rook))

        return builder.build()

    def get_highlight_tiles(self):
        return [self.get_king_destination(), self.get_rook_destination()]


class EnPassantMove(AttackingMove):

    def __init__(self, board, moved_pawn, destination, attacked_pawn):
        super().__init__(board, moved_pawn, destination)
        self.attacked_pawn = attacked_pawn

    def execute(self):
        builder = Builder()

        if self.moved_king.get_color() == 'white':
            builder.set_color_to_move('black')
        else:
            builder.set_color_to_move('white')

        for tile in self.board.board_tiles:
            builder.set_tile(tile.get_position(), tile)

        builder.set_tile(self.get_start(), EmptyTile(self.get_start()))
        new_pawn = self.moved_piece
        new_pawn.is_first_move = False
        new_pawn.position = self.get_destination()
        builder.set_tile(self.get_destination(), OccupiedTile(self.get_destination(), new_pawn))
        builder.set_tile(self.attacked_pawn.get_position(), EmptyTile(self.attacked_pawn.get_position()))

        builder.set_en_passant_pawn(None)

        return builder.build()
