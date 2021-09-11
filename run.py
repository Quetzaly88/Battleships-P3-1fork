# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint 


board = []


def make_board():
    """
    Make the starting board of X, it has no required arguments and returns the
    board
    """

    for ind in range(0, 5):
        board.append(" X "*5)
    return board


def print_board(board):
    """
    prints the board
    """
    for ind in board:
        print(ind)


def random_num(board):
    """
    Generate a random number between 0 and the length of the board minus one.
    We minus 1 because len starts at 1 but the board and arrays etc. start at 0
    """
    return randint(0, len(board)-1) 


def generate_ship_loc(board):
    ship_col = random_num(board)
    ship_row = random_num(board)
    print(ship_col, ship_row)


def main():
    make_board()
    print_board(board)
    generate_ship_loc(board)

main()

