# BRO-CODE

Two brothers coding.

## Projects:

- Tic Tac Toe
  - title at the top
  - 9 tiles
  - x goes first
  - should detect win or draw
  - display if x or o wins

## Progress:

*Includes tasks we individually need to complete. Based on our personal assessment.*

- Day 6:
  - Rio
    - Fixed global variable usage
    - Re-factor code to be more function based (still need to implement classes)
    - Implemented win logic
    - To-do:
      - Implement classes and OOP paradigm
      - Implement a way to stop the game once a player wins. (perhaps need to make into class)

- Day 5:
  - Work on TTT canvas and impelement win/turn logic
  - Brute force programming

- Day 4:
  - Made Tkinter application that converts an amount in USD to IDR (Indonesian Rupiah) and displays the result.
    - USD to IDR Conversion: Converts USD to IDR using a fixed rate (1 USD = 16,000 IDR).
    - Text Widget: Displays the converted IDR amount.
    - Entry Widget: Allows the user to input the USD amount.
    - Submit Button: Triggers the conversion and updates the Text widget.
    - Exit Button: Closes the application.
- Day 3: Python environments, git workflow, create tic tac toe basic logic
- Day 2: Understand overall goal (what resume should look like, why academic potential has been reached, why PBL is key, career trajectory, importance of internships)
- Day 1: Initialize git repo

## To do:

*These are tasks we both need to complete.*

- Re-factor code
  - Implement loops
  - Implement clases
- Classes for tiles
- Classes for markers
- Classes for game logic
- Go over vs code workflow, shortcuts
- Go over project 1
- Learn vim

## Interesting Takeaways:
*This section will be further expanded in a blog/YouTube channel.*

#### Tic-Tac-Toe Win Algorithm
The Tic-Tac-Toe win algorithm can be defined in a variety of ways. Perhaps the most general way is to calculate when a player has created a row of 3. 

What makes the definition variable is how you set up the problem in your code.

For example, the way I initially thought about this was to have all the possible winning combinations (7 of them) stored in a list.

`wins = [{1, 2, 3}, {1, 5, 9}, {1, 4, 7}, {3, 6, 9}, {3, 4, 7}, {7, 8, 9}, {2, 5, 8}]`

 I would also track both players' squares in a dictionary.
 
 `players = dict.fromkeys(["player-1", "player-2"])`
 
 After every turn, I would simply check if a winning combination existed in the dictionary. 

```
if any(wins) in players["player-1"]:
  print("Player 1 Wins!)
if any(wins) in players["player-2"]:
  print("Player 2 Wins!)
```