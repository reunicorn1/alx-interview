#!/usr/bin/python3
"""
0. N queens
"""
import sys


class QueenBoard:
    """
    This class initilizes the board instances
    """
    def __init__(self, n):
        """
        This is the constructor of the board
        """
        self.n = n
        self.board = [-1] * n
        self.valid_solutions = []

    def is_valid(self, col) -> bool:
        """
        This function validates a certain position in relation
        to the previous slots of the board where queen is placed

        Parameters:
        col: int
            the column of the queen which represent the index of the
            board in which we validate the board for

        Returns:
        A boolean of either true or false
        """
        for i in range(col):
            if (self.board[i] == self.board[col] or
                self.board[i] == self.board[col] + (col - i) or
                    self.board[i] == self.board[col] - (col - i)):
                return False
        return True

    def add_sol(self) -> None:
        """
        This function takes the current state of the board and add it
        to the valid solutions attribute
        """
        board = [[idx, row] for idx, row in enumerate(self.board)]
        print(board)
        self.valid_solutions.append(board)

    def engine(self) -> None:
        """
        This is the main engine function that generates all valid
        solutions of the nqueen puzzle

        It starts by looping through the cols and figuring out every
        possible solution that is valid and if all cols pass the answer
        is added to the valid_solutions
        """
        def inner_engine(col) -> None:
            """
            This the function that will work recursively to retrieve
            all possible combinations
            """
            if col == self.n:
                self.add_sol()
                return
            else:
                for row in range(self.n):
                    self.board[col] = row
                    if self.is_valid(col):
                        inner_engine(col + 1)
                self.board[col] = -1

        inner_engine(0)  # To initilize the mechanism of the engine


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nqueens = int(sys.argv[1])
        if nqueens < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    board = QueenBoard(nqueens)
    board.engine()
