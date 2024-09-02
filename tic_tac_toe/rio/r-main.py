"""- title at the top
  - 9 tiles
  - x goes first
  - should detect win or draw
  - display if x or o wins

    TO-DO:
    - squares are currently green/blue (implement X and Os)
    - OOP refactoring
    RESOURCES:
    - https://stackoverflow.com/questions/16988750/increment-variable-in-callback-during-upload
    - https://stackoverflow.com/questions/3431676/creating-functions-or-lambdas-in-a-loop-or-comprehension
    - https://stackoverflow.com/questions/2786877/how-to-bind-events-to-canvas-items
    - https://tkdocs.com/tutorial/firstexample.html
    - https://web.archive.org/web/20150315060716/http://effbot.org/tkinterbook/canvas.htm
    - https://web.archive.org/web/20150321101604/http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
  """

import tkinter as tk


def checkWin(event, players):
    print(players)
    wins = [{1, 2, 3}, {1, 5, 9}, {1, 4, 7}, {3, 6, 9}, {3, 4, 7}, {7, 8, 9}, {2, 5, 8}]
    ## Checking for winning combinations
    ## Iterate through wins and subtracts player squares from each winning combination
    ## If the difference results in an empty set, then player has obtained a winning combination

    center_x = game_board.winfo_width() / 2
    center_y = game_board.winfo_height() / 2
    for win in wins:
        if (win - players["player-1"]) == set():
            game_board.itemconfig("all", state="disabled")
            game_board.create_text(
                center_x, center_y, text="Player 1 wins!", font=font, fill="black"
            )
        elif (win - players["player-2"]) == set():
            game_board.itemconfig("all", state="disabled")
            game_board.create_text(
                center_x, center_y, text="Player 2 wins!", font=font, fill="black"
            )
    return None


## Fills square with color for when square is clicked
## Tracks "turn" counter to fill with either green (player 1) or blue (player 2)
def onSquareClick(event, players):
    fill = ""
    # If players have filled the same number of squares, turn goes to Player 1)
    frame.focus_set()
    if len(players["player-1"]) == len(players["player-2"]):
        fill = "green"
        players["player-1"].add(*game_board.find_withtag("current"))
    else:
        fill = "blue"
        players["player-2"].add(*game_board.find_withtag("current"))
    game_board.itemconfig("current", fill=fill, state="disabled")

    return None


def playGame(game_board):
    squares = {}  ## Keep track of squares (square idx, x0, y0, x1, y1)
    ## Keep track of turns and coordinates (only for use in creation of squares)
    coordinates = [0, 0, 0, 0]
    players = {
        "player-1": set(),
        "player-2": set(),
    }  ## Keep track of what squares each player claimed

    createSquares(game_board, coordinates, squares)
    game_board.tag_bind(
        "all", "<Button-1>", lambda event: onSquareClick(event, players)
    )

    game_board.tag_bind(
        "all", "<Button-1>", lambda event: checkWin(event, players), add="+"
    )

    return None


def createSquares(game_board, coordinates, squares):
    ## Loop for creating squares
    ## Set coordinates for first square
    ## Ofset by 50 for canvas alignment
    coordinates[1], coordinates[3] = 50, 150
    for i in range(3):
        ## For rectangles in Tk, need two endpoints for creation
        ## In each iteration, every endpoint is changing but rows and columns should be tracked separately (thus 2 for loops)
        ## First for loop tracks columns (y coordinates aks coordinates[1] & coordinates[3])
        ## Second for loop tracks rows (x coordinates aks coordinates[0] & coordinates[2])
        coordinates[0], coordinates[2] = 50, 150
        for j in range(3):
            ## Set idx from 0 - 9, taking into account structure of for loops
            idx = i * 3 + j
            ## Add squares to dictionary
            squares[idx] = (
                ## Create rectangles based on set values for coordinates
                ## Set tag names for binding
                game_board.create_rectangle(
                    *coordinates,
                    fill="white",
                    # width=1,
                    # outline="black",
                    tags=f"square_{idx}",
                ),
                *coordinates,  ## Add coordinates to dictionary
            )

            ## Spacing each square by 100
            coordinates[0] += 100
            coordinates[2] += 100
        coordinates[1] += 100
        coordinates[3] += 100


def changeTurn(players, squares):
    # x = lambda event, players=players: checkWin(players)
    pass


## Setting default settings
font = ("Verdana", 24)

root = tk.Tk()
root.title("Tic Tac Toe")
# root.resizable()

# Creating the frame for the game
frame = tk.Frame(root, width=800, height=800)
## columnconfigure/rowconfigure tells Tk that the frame should expand to fill any extra space if the window is resized
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create canvas for the board
game_board = tk.Canvas(width=400, height=400)

## Title
title = "TIC TAC TOE"
title_label = tk.Label(frame, text=title, font=font)

frame.grid()
game_board.grid()
title_label.grid()

winner = playGame(game_board)
if winner == 1:
    print("Player 1 Wins!")
elif winner == 2:
    print("Player 2 Wins!")

root.mainloop()
