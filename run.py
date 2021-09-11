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
        board.append([" X "]*5)
        ind += 1
    return board


def print_board(board):
    """
    prints the board
    """
    for ind in board:
        print(" ".join(ind))


def random_num(board):
    """
    Generate a random number between 0 and the length of the board minus one.
    We minus 1 because len starts at 1 but the board and arrays etc. start at 0
    """
    return randint(0, len(board)-1)


def generate_ship_loc(board):
    """
    Uses random_num to generate locations for battleships, updates the board
    with "o" characters to signify where the ships are for the user
    """
    for ind in range(0, 4):
        ship_col = random_num(board)
        ship_row = random_num(board)
        board[ship_col][ship_row] = " o "
        ind += 1


def main():
    """
    The function calling function
    """
    make_board()
    generate_ship_loc(board)
    print_board(board)


main()