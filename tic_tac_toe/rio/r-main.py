"""- title at the top
  - 9 tiles
  - x goes first
  - should detect win or draw
  - display if x or o wins"""

import tkinter as tk
from tkinter import ttk
    
root = tk.Tk()
frame = ttk.Frame(root)
frame.grid()

title = "TIC TAC TOE"
font = ("Verdana", 24)
title_label = tk.Label(frame, text=title, font=font)

title_label.grid()

root.mainloop()