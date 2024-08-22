import tkinter as tk
from tkinter import ttk

#global tracking variables
counter = 0
tile = 0

#when any tile is clicked, display x or o depending which turn
def click_one():
  global counter
  if counter % 2 ==0:
    tile_frame1.config(text="X", state="disabled")
    counter += 1
  else:
    tile_frame1.config(text="O", state="disabled")
    counter += 1

def click_two():
  global counter
  if counter % 2 ==0:
    tile_frame2.config(text="X", state="disabled")
    counter += 1
  else:
    tile_frame2.config(text="O", state="disabled")
    counter += 1

def click_three():
  global counter
  if counter % 2 ==0:
    tile_frame3.config(text="X", state="disabled")
    counter += 1
  else:
    tile_frame3.config(text="O", state="disabled")
    counter += 1

def click_four():
  global counter
  if counter % 2 ==0:
    tile_frame4.config(text="X", state="disabled")
    counter += 1
  else:
    tile_frame4.config(text="O", state="disabled")
    counter += 1

def click_five():
  global counter
  if counter % 2 ==0:
    tile_frame5.config(text="X", state="disabled")
    counter += 1
  else:
    tile_frame5.config(text="O", state="disabled")
    counter += 1

def click_six():
  global counter
  if counter % 2 ==0:
    tile_frame6.config(text="X", state="disabled")
    counter += 1
  else:
    tile_frame6.config(text="O", state="disabled")
    counter += 1

def click_seven():
  global counter
  if counter % 2 ==0:
    tile_frame7.config(text="X", state="disabled")
    counter += 1
  else:
    tile_frame7.config(text="O", state="disabled")
    counter += 1

def click_eight():
  global counter
  if counter % 2 ==0:
    tile_frame8.config(text="X", state="disabled")
    counter += 1
  else:
    tile_frame8.config(text="O", state="disabled")
    counter += 1

def click_nine():
  global counter
  if counter % 2 ==0:
    tile_frame9.config(text="X", state="disabled")
    counter += 1
  else:
    tile_frame9.config(text="O", state="disabled")
    counter += 1

def detect_win():
  #get text out of each tile
  one = tile_frame1['text'], two = tile_frame2['text'], three = tile_frame3['text']
  four = tile_frame4['text'], five = tile_frame5['text'], six = tile_frame6['text']
  seven = tile_frame7['text'], eight = tile_frame8['text'], nine = tile_frame9['text']

  if one == two == three:
    win_text = ttk.Label(root, text="WINNER!")



#create main window + frame for grid
root = tk.Tk()

#create title at top
title = ttk.Label(root, text="Tic Tac Bro", font=("Verdana", 20, "bold"), foreground="black")
title.grid(row=0, column=0, pady=(10, 20))

frame = ttk.Frame(root)
frame.grid(row=1, column=0, padx=10, pady=10)

#nest for loops to place tiles in grid
#for row in range(num_rows):
  #  for col in range(num_cols):

tile_frame1 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=click_one)
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
tile_frame9.grid(row=2, column=2)

root.mainloop()


"""title at the top, done
  - 9 tiles, done
  - x goes first, done
  - should detect win or draw
  - display if x or o wins"""