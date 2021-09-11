# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
board = []


def make_board():
    for ind in range(0,5):
        board.append(" X "*5)
    return board


def print_board(board):
    for ind in board:
        print(ind)


make_board()
print_board(board)