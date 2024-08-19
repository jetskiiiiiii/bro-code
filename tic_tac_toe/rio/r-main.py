"""- title at the top
  - 9 tiles
  - x goes first
  - should detect win or draw
  - display if x or o wins"""

import tkinter as tk
from tkinter import ttk

# class Tiles():
#       def __init__(self) -> None:
#             self.
    
def savePosn(event):
  global lastx, lasty
  lastx, lasty = event.x, event.y

def addLine(event):
  game_board.create_line((lastx, lasty, event.x, event.y))
  savePosn(event)
  
    
root = tk.Tk()
root.title("Tic Tac Toe")

frame = ttk.Frame(root)
frame.grid()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

title = "TIC TAC TOE"
font = ("Verdana", 24)
title_label = tk.Label(frame, text=title, font=font)

# for i in range(9):
#       new Tiles

game_board = tk.Canvas(root)
game_board.grid(column=0, row=1)

game_board.bind("<Button-1>", savePosn)
game_board.bind("<B1-Motion>", addLine)

title_label.grid()

root.mainloop()