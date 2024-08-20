import tkinter as tk
from tkinter import ttk

#create function to track user clicks
def user_click():
  counter = 0
  if counter % 2 == 0:
       if n == 1:
         pass
         #tile_frame1.config(text="X") #print x on grid
       if n == 2:
        tile_frame2.config(text="X")
       if n == 3:
        tile_frame3.config(text="X") 

        
       counter += 1
  
  else:
     #print o on grid
     #tile_frame1.config(text="O")
     counter += 1

#create main window + frame for grid
root = tk.Tk()

#create title at top
title = ttk.Label(root, text="Tic Tac Bro", font=("Verdana", 20, "bold"), foreground="black")
title.grid(row=0, column=0, pady=(10, 20))

frame = ttk.Frame(root)
frame.grid(row=1, column=0, padx=10, pady=10)

#define grid dimensions
num_rows = 3
num_cols = 3

#nest for loops to place tiles in grid
#for row in range(num_rows):
  #  for col in range(num_cols):

#tile_frame1 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=user_click(1))
#tile_frame1.grid(row=0, column=0)

tile_frame2 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=user_click)
tile_frame2.grid(row=0, column=1)

tile_frame3 = tk.Button(frame, width=20, height=10, relief="ridge", borderwidth=2, command=user_click)
tile_frame3.grid(row=0, column=2)
        

root.mainloop()


"""title at the top, done
  - 9 tiles, done
  - x goes first
  - should detect win or draw
  - display if x or o wins"""