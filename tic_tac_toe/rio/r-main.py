"""- title at the top
  - 9 tiles
  - x goes first
  - should detect win or draw
  - display if x or o wins"""

import tkinter as tk

# class Tiles(tk.Canvas):
#   def __init__(self, shape) -> None:
#     super().__init__()
#     self.shape = shape

#     tile = tk.Canvas

#   def draw(self):

root = tk.Tk()
root.title("Tic Tac Toe")
# root.resizable()

frame = tk.Frame(root, width=800, height=800)
frame.grid()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

game_board = tk.Canvas(width=400, height=400)

# Title
title = "TIC TAC TOE"
font = ("Verdana", 24)
title_label = tk.Label(frame, text=title, font=font)

# sqr = game_board.create_rectangle(0, 0, 400, 400, fill="white")

squares = {}
y0, y1 = 50, 150
for i in range(3):
    x0, x1 = 50, 150
    for j in range(3):
        # set idx from 0 - 9
        idx = i * 3 + j
        print(idx, x0, y0, x1, y1)
        squares[f"square_{idx}"] = game_board.create_rectangle(
            x0, y0, x1, y1, fill="white", width=1, outline="black"
        )
        x0 += 100
        x1 += 100
    y0 += 100
    y1 += 100

squares[0].b

# print(len(squares))
# square_1 = game_board.create_rectangle(0, 0, 100, 100, fill="white")
# square_2 = game_board.create_rectangle(100, 0, 200, 100, fill="white")
# square_3 = game_board.create_rectangle(200, 0, 300, 100, fill="white")
# square_3 = game_board.create_rectangle(0, 100, 100, 200, fill="white")

game_board.grid()
title_label.grid()

root.mainloop()
