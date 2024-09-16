import tkinter as tk
from tkinter import ttk

"""
- https://web.archive.org/web/20150315060716/http://effbot.org/tkinterbook/canvas.htm
- https://web.archive.org/web/20150321101604/http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
"""


def detectWin():
  wins = [
        {1, 2, 3},
        {1, 5, 9},
        {1, 4, 7},
        {3, 6, 9},
        {3, 4, 7},
        {7, 8, 9},
        {2, 5, 8},
        {4, 5, 6},
        {3, 5, 7},
    ]
  
  x_win = ttk.Label(root, text="PLAYER 1 WINS!", font=("Verdana", 20)) #display when x wins
  o_win = ttk.Label(root, text="PLAYER 2 WINS!", font=("Verdana", 20)) #display when o wins
     

#create main window + frame for grid
root = tk.Tk()

#create title at top
title = ttk.Label(root, text="Tic Tac Bro", font=("Verdana", 20, "bold"), foreground="black")
title.grid(row=0, column=0, pady=(10, 20))

#create frame for grid to be placed in row 2
frame = ttk.Frame(root)
frame.grid(row=1, column=0, padx=10, pady=10)


def click(button_tracker, turn_count):
  detectWin()

  if turn_count % 2 == 1:
    button_tracker[turn_count].config(text="X", state="disabled")
  else:
    button_tracker[turn_count].config(text="O", state="disabled")


def createSquare(button_tracker, row, column, turn_count):
  tile_frame = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=lambda: click(button_tracker, turn_count))
  tile_frame.grid(row=row, column=column)
  button_tracker.append(tile_frame)
  return button_tracker, turn_count + 1


def playGame():
  button_tracker = []
  turn_count = 0

  for row in range(3):
    for column in range(3):
      button_tracker, turn_count = createSquare(button_tracker, row, column, turn_count)



    
#print(button_tracker)

playGame()
root.mainloop()

"""title at the top
  - 9 tiles
  - x goes first
  - should detect win or draw
  - display if x or o wins"""