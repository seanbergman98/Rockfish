from tkinter import *
from PIL import Image, ImageTk


def start_game(game_mode):
    start_window.destroy()
    game_window = Tk()
    game_window.geometry('800x500')
    game_window.resizable(width=False, height=False)
    game_window.configure(bg='#282828')
    game_window.title('Rockfish')
    game_window.iconbitmap('art/Papirus-Team-Papirus-Apps-Chess.ico')

    if game_mode == 'computer':
        print('Seems okay')


start_window = Tk()
start_window.geometry('800x500')
start_window.resizable(width=False, height=False)
start_window.configure(bg='#282828')
start_window.title('Rockfish')
start_window.iconbitmap('art/Papirus-Team-Papirus-Apps-Chess.ico')

play_human_button = Button(start_window, text='Play vs another human', bg='#505050', command=lambda: start_game('human'))
play_computer_button = Button(start_window, text='Play vs computer', bg='#505050', command=lambda: start_game('computer'))

play_human_button.pack()
play_computer_button.pack()


start_window.mainloop()

