"""- title at the top
  - 9 tiles
  - x goes first
  - should detect win or draw
  - display if x or o wins

    TO-DO:
    - squares are currently green/blue (implement X and Os)
    - win logic
    - OOP refactoring
    RESOURCES:
    - https://stackoverflow.com/questions/16988750/increment-variable-in-callback-during-upload
    - https://stackoverflow.com/questions/3431676/creating-functions-or-lambdas-in-a-loop-or-comprehension
    - https://stackoverflow.com/questions/2786877/how-to-bind-events-to-canvas-items
    - https://tkdocs.com/tutorial/firstexample.html
  """

import tkinter as tk


def checkWin(players):
    wins = [{1, 2, 3}, {1, 5, 9}, {1, 4, 7}, {3, 6, 9}, {3, 4, 7}, {7, 8, 9}, {2, 5, 8}]
    ## Checking for winning combinations
    if any(wins) in players["player-1"]:
        return 1
    if any(wins) in players["player-2"]:
        return 2
    return None


## Fills square with color for when square is clicked
## Tracks "turn" counter to fill with either green (player 1) or blue (player 2)
def onSquareClick(idx, squares, turn, players):
    fill = ""
    if turn % 2 == 0:
        fill = "green"
        players.update({"player-1": idx})
    else:
        fill = "blue"
        players.update({"player-2": idx})
    game_board.create_rectangle(
        *squares[idx][1:5], fill=fill
    )  ## Uses unpacking variable to get coordinates
    checkWin()
    return turn + 1, players


def playGame(game_board):
    squares = {}  ## Keep track of squares (square idx, x0, y0, x1, y1)
    ## Keep track of turns and coordinates (only for use in creation of squares)
    turn = 0
    coordinates = [0, 0, 0, 0]
    players = dict.fromkeys(
        ["player-1", "player-2"]
    )  ## Keep track of what squares each player claimed

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

            ## Add bindings to each square
            game_board.tag_bind(
                f"square_{idx}",  ## Reference by tags
                "<Button-1>",  ## Set sequence (mouse click is set as Button-# in documentation)
                lambda event, idx=idx: onSquareClick(  ## This is causing problems! As the callback doesn't have a way to return values.
                    idx, squares, turn, players
                ),  ## Using lambda to run callback and force early binding (so idx is tracked)
            )
            ## Spacing each square by 100
            coordinates[0] += 100
            coordinates[2] += 100
        coordinates[1] += 100
        coordinates[3] += 100


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
