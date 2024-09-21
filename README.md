# Tic-Tac-Toe-Game-with-display-board

Tic-Tac-Toe Game in Python
Overview
This is a simple console-based Tic-Tac-Toe game built in Python. The game allows two players to play against each other on a 3x3 grid. Players take turns placing their marks (X or O) on the board, and the first to get three marks in a row (horizontally, vertically, or diagonally) wins the game. If the board is filled without a winner, the game ends in a draw.

Features
Two-player mode: Play with a friend in a turn-based manner.
Board display: Visual representation of the Tic-Tac-Toe board after each move.
Input validation: Ensures players enter valid moves.
Winner detection: Automatically detects when a player has won or if the game is a draw.
How to Run
Make sure you have Python installed on your machine (Python 3.x is recommended).
Clone this repository or download the script file.
Run the game in the terminal/command prompt:
bash
Copy code
python main.py
Follow the instructions in the console to play the game.
How to Play
The game is played on a 3x3 grid.
Player 1 uses the symbol X, and Player 2 uses O.
Players take turns choosing a position on the board by entering the corresponding number (1-9).
The first player to get three marks in a row (horizontally, vertically, or diagonally) wins the game.
If all spaces are filled and no player has three in a row, the game ends in a draw.
Board Layout
markdown
Copy code
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
Example Gameplay
markdown
Copy code
Player 1's turn: Enter a number (1-9):
5

Board after Player 1's move:
   |   |   
---------
 X |   |   
---------
   |   |   

Player 2's turn: Enter a number (1-9):
1

Board after Player 2's move:
 O |   |   
---------
 X |   |   
---------
   |   |   
Future Improvements
Add a single-player mode with an AI opponent.
Implement a graphical user interface (GUI) using libraries like tkinter.
Add a scoreboard to track wins, losses, and draws.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the Python community and various online tutorials for inspiring this project!
