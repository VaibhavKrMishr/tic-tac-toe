import tkinter as tk
from tkinter import messagebox

# Constants for the grid size and winning condition
GRID_SIZE = 4
WINNING_COUNT = 3

# Player constants
NONE = 0
PLAYER_X = 1
PLAYER_O = 2

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe (4x4)")

        self.show_rules()

        self.start_game()

    def start_game(self):
        self.current_player = PLAYER_X
        self.game_over = False
        self.board = [[NONE for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        # Create the buttons for the 4x4 grid
        self.buttons = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def show_rules(self):
        rules = (
            "Welcome to Tic-Tac-Toe (4x4)!\n\n"
            "Player 1: X\n"
            "Player 1: O\n\n"
            "The goal is to get 3 continuous marks (X or O) in a row, column, or diagonal.\n"
            "Click on a cell to make your move.\n\n"
            "Player 1:X starts first."
        )
        messagebox.showinfo("Game Rules", rules)

    def make_move(self, row, col):
        if self.game_over or self.board[row][col] != NONE:
            return

        # Set the current player's mark (X or O)
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text="X" if self.current_player == PLAYER_X else "O")

        # Check for a win or draw
        if self.check_win(row, col):
            self.game_over = True
            messagebox.showinfo("Game Over", f"Player {'X' if self.current_player == PLAYER_X else 'O'} wins!")
            self.reset_game()
        elif self.check_draw():
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()

        # Switch to the next player
        self.current_player = PLAYER_X if self.current_player == PLAYER_O else PLAYER_O

    def check_win(self, row, col):
        # Check for winning condition by ensuring 3 consecutive marks
        return self.check_row(row) or self.check_col(col) or self.check_diagonals()

    def check_row(self, row):
        # Check if there are 3 consecutive marks in the row
        for col in range(GRID_SIZE - WINNING_COUNT + 1):
            if all(self.board[row][col + i] == self.current_player for i in range(WINNING_COUNT)):
                return True
        return False

    def check_col(self, col):
        # Check if there are 3 consecutive marks in the column
        for row in range(GRID_SIZE - WINNING_COUNT + 1):
            if all(self.board[row + i][col] == self.current_player for i in range(WINNING_COUNT)):
                return True
        return False

    def check_diagonals(self):
        # Check top-left to bottom-right diagonals
        for start_row in range(GRID_SIZE - WINNING_COUNT + 1):
            for start_col in range(GRID_SIZE - WINNING_COUNT + 1):
                if all(self.board[start_row + i][start_col + i] == self.current_player for i in range(WINNING_COUNT)):
                    return True

        # Check top-right to bottom-left diagonals
        for start_row in range(GRID_SIZE - WINNING_COUNT + 1):
            for start_col in range(WINNING_COUNT - 1, GRID_SIZE):
                if all(self.board[start_row + i][start_col - i] == self.current_player for i in range(WINNING_COUNT)):
                    return True

        return False

    def check_draw(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] == NONE:
                    return False
        return True

    def reset_game(self):
        """Reset the game and prepare for a new round."""
        self.game_over = False
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                self.board[row][col] = NONE
                self.buttons[row][col].config(text="")
        self.current_player = PLAYER_X  # Start with Player X after resetting the game

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
