# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint


board_user = []
board_user_guesses = []
board_comp = []


def make_board(board):
    """
    Make the starting board of X
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
    # note that it is possible to have the same random numbers twice so less
    # than 4 ships to aim for which would make the game unfair


def welcome():
    """
    Opening message to the game
    """
    print("Welcome to you vs. computer Battleships!")
    username = input("Type in a username and press return: ")
    print(f"Hi {username}! We will auto generate your battleship locations. You have 4 battleships to find within the computer's board")
    print("Here is the computer's board:")
    print_board(board_user_guesses)



def main():
    """
    The function calling function
    """
    make_board(board_user)
    make_board(board_comp)
    make_board(board_user_guesses)
    generate_ship_loc(board_user)
    generate_ship_loc(board_comp)
    

def welcome():
    """
    Opening message to the game
    """
    print("Welcome to you vs. computer Battleships!")
    username = input("Type in a username and press return: ")
    print(f"Hi {username}! We will auto generate your battleship locations. You have 4 battleships to find within the computer's board")
    print("Here is the computer's board:")
    print_board(board_user_guesses)

def user_guess():
    """
    Get user input on battleship guess
    """
    guess_col = int(input("Which column would you like to fire at? Enter a number and press enter:"))
    guess_row = int(input("Which row would you like to fire at? Enter a number and press enter:"))  
    if board_comp[guess_col][guess_row] == " o ":
        board_user_guesses[guess_col][guess_row] = " # "
    else:
        board_user_guesses[guess_col][guess_row] = " * "
    print_board(board_user_guesses)

main()
welcome()
user_guess()