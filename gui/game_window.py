from tkinter import *
from PIL import ImageTk, Image

from engine.board.board import Board
from gui.gameboard_panel import GameBoardPanel


class GameWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title('Rockfish')
        self.iconbitmap('C:/Users/seanb/Documents/Rockfish/art/Papirus-Team-Papirus-Apps-Chess.ico')
        self.gameboard_panel = GameBoardPanel(self, 'white', Board.create_starting_board())
        self.gameboard_panel.pack()


game_window = GameWindow()
game_window.mainloop()

