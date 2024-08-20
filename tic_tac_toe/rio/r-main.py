"""- title at the top
  - 9 tiles
  - x goes first
  - should detect win or draw
  - display if x or o wins"""

import tkinter as tk
from tkinter import ttk

# class Tiles(tk.Canvas):
#   def __init__(self, shape) -> None:
#     super().__init__()
#     self.shape = shape

#     tile = tk.Canvas

#   def draw(self):


root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable()

frame = ttk.Frame(root)
frame.grid()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

game_board = tk.Canvas()

# Title
title = "TIC TAC TOE"
font = ("Verdana", 24)
title_label = tk.Label(frame, text=title, font=font)

game_board.create_rectangle(1, 1, 100, 100, fill="white")

game_board.grid()
title_label.grid()

root.mainloop()
