import tkinter as tk
from tkinter import ttk

#create function to track user clicks
def user_click():


#create main window + frame for grid
root = tk.Tk()

#create title at top
title = ttk.Label(root, text="Tic Tac Bro", font=("Verdana", 20, "bold"), background="black", foreground="white")
title.grid(row=0, column=0, pady=(10, 20))

frame = ttk.Frame(root)
frame.grid(row=1, column=0, padx=10, pady=10)

#define grid dimensions
num_rows = 3
num_cols = 3

#nest for loops to place tiles in grid
for row in range(num_rows):
    for col in range(num_cols):
        tile_frame = ttk.Frame(frame, width=100, height=100, relief="ridge", borderwidth=2)
        tile_frame.grid(row=row, column=col)

        

root.mainloop()


"""title at the top, done
  - 9 tiles, done
  - x goes first
  - should detect win or draw
  - display if x or o wins"""