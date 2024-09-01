import tkinter as tk
from tkinter import ttk

#global tracking variables
counter = 0
tile = 0

#when any tile is clicked, display x or o depending which turn and check for winner after each display
def click_one(s):
  global counter
  if counter % 2 ==0:
    #tile_frame1.config(text="X", state="disabled")
    counter += 1
    #detect_win()
  else:
    #tile_frame1.config(text="O", state="disabled")
    counter += 1
    #detect_win()

def click_two():
  global counter
  if counter % 2 ==0:
    tile_frame2.config(text="X", state="disabled")
    counter += 1
    detect_win()
  else:
    tile_frame2.config(text="O", state="disabled")
    counter += 1
    detect_win()

def click_three():
  global counter
  if counter % 2 ==0:
    tile_frame3.config(text="X", state="disabled")
    counter += 1
    detect_win()
  else:
    tile_frame3.config(text="O", state="disabled")
    counter += 1
    detect_win()

def click_four():
  global counter
  if counter % 2 ==0:
    tile_frame4.config(text="X", state="disabled")
    counter += 1
    detect_win()
  else:
    tile_frame4.config(text="O", state="disabled")
    counter += 1
    detect_win()

def click_five():
  global counter
  if counter % 2 ==0:
    tile_frame5.config(text="X", state="disabled")
    counter += 1
    detect_win()
  else:
    tile_frame5.config(text="O", state="disabled")
    counter += 1
    detect_win()

def click_six():
  global counter
  if counter % 2 ==0:
    tile_frame6.config(text="X", state="disabled")
    counter += 1
    detect_win()
  else:
    tile_frame6.config(text="O", state="disabled")
    counter += 1
    detect_win()

def click_seven():
  global counter
  if counter % 2 ==0:
    tile_frame7.config(text="X", state="disabled")
    counter += 1
    detect_win()
  else:
    tile_frame7.config(text="O", state="disabled")
    counter += 1
    detect_win()

def click_eight():
  global counter
  if counter % 2 ==0:
    tile_frame8.config(text="X", state="disabled")
    counter += 1
    detect_win()
  else:
    tile_frame8.config(text="O", state="disabled")
    counter += 1
    detect_win()

def click_nine():
  global counter
  if counter % 2 ==0:
    tile_frame9.config(text="X", state="disabled")
    counter += 1
    detect_win()
  else:
    tile_frame9.config(text="O", state="disabled")
    counter += 1
    detect_win()

def disable_buttons(): #function to disable buttons after win
  tile_frame1.config(state="disabled")
  tile_frame2.config(state="disabled")
  tile_frame3.config(state="disabled")
  tile_frame4.config(state="disabled")
  tile_frame5.config(state="disabled")
  tile_frame6.config(state="disabled")
  tile_frame7.config(state="disabled")
  tile_frame8.config(state="disabled")
  tile_frame9.config(state="disabled")

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

def click(button):
  if button % 2 == 1:
    print("X")
  else:
    print("O")


#make each tile as a button, run user click function when clicked
button_tracker = []
button = 0

for row in range(3):
  for column in range(3):
    tile_frame = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=lambda button=button:click(button))
    tile_frame.grid(row=row, column=column)
    button += 1
    button_tracker.append(tile_frame)
    
print(button_tracker)
"""tile_frame1 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=click_one)
tile_frame1.grid(row=0, column=0)

tile_frame2 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=click_two)
tile_frame2.grid(row=0, column=1)

tile_frame3 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=click_three)
tile_frame3.grid(row=0, column=2)
        
tile_frame4 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=click_four)
tile_frame4.grid(row=1, column=0)

tile_frame5 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=click_five)
tile_frame5.grid(row=1, column=1)

tile_frame6 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=click_six)
tile_frame6.grid(row=1, column=2)

tile_frame7 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=click_seven)
tile_frame7.grid(row=2, column=0)

tile_frame8 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=click_eight)
tile_frame8.grid(row=2, column=1)

tile_frame9 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=click_nine)
tile_frame9.grid(row=2, column=2)"""

root.mainloop()


"""title at the top, done
  - 9 tiles, done
  - x goes first, done
  - should detect win or draw
  - display if x or o wins"""