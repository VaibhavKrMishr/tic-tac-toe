Tic-Tac-Toe (4x4) Game
Description
This is a Python implementation of the classic Tic-Tac-Toe game with a 4x4 grid, where the objective is to get 3 continuous marks (either X or O) in a row, column, or diagonal. The game is built using Tkinter for the graphical user interface (GUI). The game alternates between two players (Player X and Player O), and the player who successfully aligns 3 consecutive marks wins.

Features
4x4 Grid: The game board is a 4x4 grid where players can make their moves.
3 Consecutive Marks to Win: To win, a player needs to align 3 continuous marks either in a row, column, or diagonal.
Player Turn Alternation: The game alternates between Player X and Player O.
Draw Condition: The game will declare a draw if there are no more moves left and no winner.
Game Reset: After a win or draw, the game automatically resets for a new round.
Rules Display: The game shows a pop-up with the rules at the beginning.
Requirements
Python 3.x
Tkinter (usually comes pre-installed with Python)
How to Run
Make sure you have Python 3 installed on your system. Tkinter is usually bundled with Python, so no need to install it separately.

Save the code provided in a Python file, for example, tictactoe.py.

Run the game by executing the following command in your terminal/command prompt:

bash
Copy code
python tictactoe.py
The game window will open, displaying a 4x4 grid. Follow the on-screen instructions to play.

Gameplay
The game starts with Player X.
Click on any empty cell to place your mark (X or O).
The game will check after each move for a winner or a draw.
Once a player wins or the game ends in a draw, a message box will pop up announcing the result. The game will then automatically reset for a new round, with Player X starting again.
Game Rules
Player 1 is X, and Player 2 is O.
The goal is to get 3 continuous marks (either X or O) in a row, column, or diagonal.
The game will end when one player wins or when all cells are filled, resulting in a draw.