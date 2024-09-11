import tkinter as tk
from tkinter import ttk

"""
- https://web.archive.org/web/20150315060716/http://effbot.org/tkinterbook/canvas.htm
- https://web.archive.org/web/20150321101604/http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
"""
#global tracking variables
counter = 0
tile = 0


"""def disable_buttons(): #function to disable buttons after win
  tile_frame1.config(state="disabled")
  tile_frame2.config(state="disabled")
  tile_frame3.config(state="disabled")
  tile_frame4.config(state="disabled")
  tile_frame5.config(state="disabled")
  tile_frame6.config(state="disabled")
  tile_frame7.config(state="disabled")
  tile_frame8.config(state="disabled")
  tile_frame9.config(state="disabled")"""

def detect_win():
  x_win = ttk.Label(root, text="PLAYER 1 WINS!", font=("Verdana", 20)) #display when x wins
  o_win = ttk.Label(root, text="PLAYER 2 WINS!", font=("Verdana", 20)) #display when o wins

  #get text out of each tile
  one = tile_frame1['text']
  two = tile_frame2['text']
  three = tile_frame3['text']
  four = tile_frame4['text']
  five = tile_frame5['text']
  six = tile_frame6['text']
  seven = tile_frame7['text']
  eight = tile_frame8['text']
  nine = tile_frame9['text']

#check for eight different win scenarios, display x wins if true
  if one == two == three == "X":
    x_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if one == four == seven == "X":
    x_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if one == five == nine == "X":
    x_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if two == five == eight == "X":
    x_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if three == six == nine == "X":
    x_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if three == five == seven == "X":
    x_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if four == five == six == "X":
    x_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if seven == eight == nine == "X":
    x_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()

  if one == two == three == "O":
    o_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if one == four == seven == "O":
    o_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if one == five == nine == "O":
    o_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if two == five == eight == "O":
    o_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if three == six == nine == "O":
    o_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if three == five == seven == "O":
    o_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if four == five == six == "O":
    o_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()
  if seven == eight == nine == "O":
    o_win.grid(row=2, column=0, pady=(10, 20))
    disable_buttons()

#create main window + frame for grid
root = tk.Tk()

#create title at top
title = ttk.Label(root, text="Tic Tac Bro", font=("Verdana", 20, "bold"), foreground="black")
title.grid(row=0, column=0, pady=(10, 20))

#create frame for grid to be placed in row 2
frame = ttk.Frame(root)
frame.grid(row=1, column=0, padx=10, pady=10)


def click(button, button_tracker, turn_count):
  if turn_count % 2 == 1:
    #print("X")
    button_tracker[button].config(text="X", state="disabled")
  else:
    #print("O")
    button_tracker[button].config(text="O", state="disabled")


def createSquare(button_tracker, row, column):
  tile_frame = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2)
  tile_frame.grid(row=row, column=column)
  button_tracker.append(tile_frame)
  return button_tracker


def playGame():
  button_tracker = []
  button = 0
  turn_count = 0

  for row in range(3):
    for column in range(3):
      button_tracker = createSquare(button_tracker, row, column)

  while turn_count < 9:
    click(button, button_tracker, turn_count)
    turn_count += 1



    
#print(button_tracker)

playGame()
root.mainloop()

"""title at the top, done
  - 9 tiles, done
  - x goes first, done
  - should detect win or draw
  - display if x or o wins"""