from tkinter import *
from abc import ABC, abstractmethod
from PIL import ImageTk, Image

from engine.board.board_utils import NUM_TILES, NUM_TILES_PER_ROW
from engine.board.move import Move

LIGHT_TILE = '#F0D9B5'
DARK_TILE = '#B58863'
LIGHT_TILE_SELECTED = '#829769'
DARK_TILE_SELECTED = '#646F40'
LIGHT_TILE_MOVED = '#CDD26A'
DARK_TILE_MOVED = '#AAA23A'
LIGHT_TILE_CANDIDATE = '#AEB27F'
DARK_TILE_CANDIDATE = '#857945'

CANDIDATE_CIRCLE_RADIUS = 8

TILE_DIMENSION = 60
BOARD_DIMENSION = TILE_DIMENSION * 8

WHITE_PAWN = 'art/Chess_plt60.png'
WHITE_ROOK = 'art/Chess_rlt60.png'
WHITE_KNIGHT = 'art/Chess_nlt60.png'
WHITE_BISHOP = 'art/Chess_blt60.png'
WHITE_QUEEN = 'art/Chess_qlt60.png'
WHITE_KING = 'art/Chess_klt60.png'

BLACK_PAWN = 'art/Chess_pdt60.png'
BLACK_ROOK = 'art/Chess_rdt60.png'
BLACK_KNIGHT = 'art/Chess_ndt60.png'
BLACK_BISHOP = 'art/Chess_bdt60.png'
BLACK_QUEEN = 'art/Chess_qdt60.png'
BLACK_KING = 'art/Chess_kdt60.png'


def get_coordinates(position, orientation):
    if orientation == 'white':
        column = position % NUM_TILES_PER_ROW
        row = 7 - position // NUM_TILES_PER_ROW
    else:
        column = 7 - position % NUM_TILES_PER_ROW
        row = position // NUM_TILES_PER_ROW

    return column, row


class GameBoardPanel(Frame):

    def __init__(self, game_window, orientation, board, selected_piece=None, last_move=None):
        super().__init__(game_window, width=BOARD_DIMENSION, height=BOARD_DIMENSION)
        self.game_window = game_window
        self.orientation = orientation
        self.selected_piece = selected_piece
        self.last_move = last_move
        self.board = board

        if self.selected_piece is not None:
            self.legal_move_destinations = map(lambda x: x.get_destination(), self.selected_piece.get_legal_moves(self.board))
        else:
            self.legal_move_destinations = []

        self.create_tiles()

    def create_tiles(self):

        for position in range(NUM_TILES):

            x, y = get_coordinates(position, self.orientation)

            #Check if the given tile is a light tile
            if (x + y) % 2 == 0:
                #Check if there is a selected tile
                if self.selected_piece is not None:
                    #If there is a selected tile, check if the current tile is the selected tile
                    if position == self.selected_piece.get_position():
                        background = LIGHT_TILE_SELECTED
                    elif self.last_move is not None:
                        if position in self.last_move.get_highlight_positions():
                            background = LIGHT_TILE_MOVED
                        else:
                            background = LIGHT_TILE_MOVED
                    else:
                        background = LIGHT_TILE
                #Otherwise there is no selected tile
                else:
                    if self.last_move is not None:
                        if position in self.last_move.get_highlight_positions():
                            background = LIGHT_TILE_MOVED
                        else:
                            background = LIGHT_TILE_MOVED
                    else:
                        background = LIGHT_TILE
            #Otherwise we must have a dark tile
            else:
                # Check if there is a selected tile
                if self.selected_piece is not None:
                    # If there is a selected tile, check if the current tile is the selected tile
                    if position == self.selected_piece.get_position():
                        background = DARK_TILE_SELECTED
                    elif self.last_move is not None:
                        if position in self.last_move.get_highlight_positions():
                            background = DARK_TILE_MOVED
                        else:
                            background = DARK_TILE_MOVED
                    else:
                        background = DARK_TILE
                # Otherwise there is no selected tile
                else:
                    if self.last_move is not None:
                        if position in self.last_move.get_highlight_positions():
                            background = DARK_TILE_MOVED
                        else:
                            background = DARK_TILE_MOVED
                    else:
                        background = DARK_TILE

            tile = self.board.get_tile(position)
            piece = tile.get_piece()

            tile_panel = TilePanel(self.game_window, self, position, piece, self.selected_piece,
                                   self.last_move, self.board, background)

            #Check to see if the given tile panel should be highlighted as a candidate destination
            if position in self.legal_move_destinations:
                if (x + y) % 2 == 0:
                    if tile.is_tile_occupied():
                        #Identical behaviour for now, but should ultimately emulate lichess
                        tile_panel.create_oval(TILE_DIMENSION - CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION - CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION + CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION + CANDIDATE_CIRCLE_RADIUS,
                                               fill=LIGHT_TILE_CANDIDATE)
                    else:
                        tile_panel.create_oval(TILE_DIMENSION - CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION - CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION + CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION + CANDIDATE_CIRCLE_RADIUS,
                                               fill=LIGHT_TILE_CANDIDATE)
                else:
                    if tile.is_tile_occupied():
                        #Again, identical behaviour for now
                        tile_panel.create_oval(TILE_DIMENSION - CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION - CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION + CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION + CANDIDATE_CIRCLE_RADIUS,
                                               fill=DARK_TILE_CANDIDATE)
                    else:
                        tile_panel.create_oval(TILE_DIMENSION - CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION - CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION + CANDIDATE_CIRCLE_RADIUS,
                                               TILE_DIMENSION + CANDIDATE_CIRCLE_RADIUS,
                                               fill=DARK_TILE_CANDIDATE)

            tile_panel.grid(row=y, column=x, sticky='NSEW')


class TilePanel(Canvas):

    def __init__(self, game_window, gameboard_panel, position, piece, selected_piece, last_move, board, background):
        super().__init__(gameboard_panel, width=TILE_DIMENSION, height=TILE_DIMENSION, bg=background, highlightthickness=0)
        self.game_window = game_window
        self.position = position
        self.piece = piece
        self.selected_piece = selected_piece
        self.last_move = last_move
        self.board = board
        self.set_piece_image()
        self.draw_piece()
        self.bind('<Button-1>', self.click)

    def set_piece_image(self):
        if self.piece is not None:
            piece_type = self.piece.get_piece_type()
            if self.piece.get_color() == 'white':
                if piece_type == 'pawn':
                    self.piece_image = ImageTk.PhotoImage(Image.open(WHITE_PAWN))
                elif piece_type == 'rook':
                    self.piece_image = ImageTk.PhotoImage(Image.open(WHITE_ROOK))
                elif piece_type == 'knight':
                    self.piece_image = ImageTk.PhotoImage(Image.open(WHITE_KNIGHT))
                elif piece_type == 'bishop':
                    self.piece_image = ImageTk.PhotoImage(Image.open(WHITE_BISHOP))
                elif piece_type == 'queen':
                    self.piece_image = ImageTk.PhotoImage(Image.open(WHITE_QUEEN))
                elif piece_type == 'king':
                    self.piece_image = ImageTk.PhotoImage(Image.open(WHITE_KING))
            else:
                if piece_type == 'pawn':
                    self.piece_image = ImageTk.PhotoImage(Image.open(BLACK_PAWN))
                elif piece_type == 'rook':
                    self.piece_image = ImageTk.PhotoImage(Image.open(BLACK_ROOK))
                elif piece_type == 'knight':
                    self.piece_image = ImageTk.PhotoImage(Image.open(BLACK_KNIGHT))
                elif piece_type == 'bishop':
                    self.piece_image = ImageTk.PhotoImage(Image.open(BLACK_BISHOP))
                elif piece_type == 'queen':
                    self.piece_image = ImageTk.PhotoImage(Image.open(BLACK_QUEEN))
                elif piece_type == 'king':
                    self.piece_image = ImageTk.PhotoImage(Image.open(BLACK_KING))
        else:
            self.piece_image = None

    def draw_piece(self):
        if self.piece_image is not None:
            self.create_image(TILE_DIMENSION / 2, TILE_DIMENSION / 2, anchor=CENTER, image=self.piece_image)

    def click(self, event):

        if self.selected_piece is not None:

            if self.position in map(lambda x: x.get_position(), self.board.get_active_pieces()):
                self.game_window.gameboard_panel.destroy()
                self.game_window.gameboard_panel = GameBoardPanel(self.game_window, 'white', self.board,
                                                                  selected_piece=self.piece, last_move=self.last_move)
                self.game_window.gameboard_panel.pack()

            elif self.position in map(lambda x: x.get_destination(), self.selected_piece.get_legal_moves(self.board)):
                move = Move(self.board, self.selected_piece, self.position)
                new_board = move.execute()
                self.game_window.gameboard_panel.destroy()
                self.game_window.gameboard_panel = GameBoardPanel(self.game_window, 'white', new_board)
                self.game_window.gameboard_panel.pack()

            else:
                self.game_window.gameboard_panel.destroy()
                self.game_window.gameboard_panel = GameBoardPanel(self.game_window, 'white', self.board,
                                                                  last_move=self.last_move)
                self.game_window.gameboard_panel.pack()

        else:
            if self.position in map(lambda x: x.get_position(), self.board.get_active_pieces()):
                self.game_window.gameboard_panel.destroy()
                self.game_window.gameboard_panel = GameBoardPanel(self.game_window, 'white', self.board,
                                                                  selected_piece=self.piece, last_move=self.last_move)
                self.game_window.gameboard_panel.pack()
