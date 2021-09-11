# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# So we've got turns, we've got guess inputs, guess random num, we've got checking if it's a hit/miss
# Need: Exception handling
# Need: Checking for a winner. This might be that all the ships are found or it might be who has the most hits.

from random import randint


user = []
user_guesses = []
comp = []


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
    print_board(user_guesses)


def main():
    """
    The function calling function
    """
    make_board(user)
    make_board(comp)
    make_board(user_guesses)
    generate_ship_loc(user)
    generate_ship_loc(comp)


def welcome():
    """
    Opening message to the game
    """
    print("Welcome to you vs. computer Battleships!")
    username = input("Type in a username and press return: ")
    print(f"Hi {username}! We will auto generate your battleship locations. You have 4 battleships to find within the computer's board")
    

def user_guess():
    """
    Get user input on battleship guess
    """
    print("Here is the computer's board:")
    print_board(user_guesses)
    print("Which column would you like to fire at?")
    guess_col = int(input("Enter a number and press enter: "))
    print("Which row would you like to fire at?")
    guess_row = int(input("Enter a number and press enter: "))  
    if comp[guess_col][guess_row] == " o ":
        user_guesses[guess_col][guess_row] = " # "
        print("YAY! You hit their ship!")
    else:
        user_guesses[guess_col][guess_row] = " * "
        print("Oh no! You missed their ship :(")
    print_board(user_guesses)


def comp_guess():
    """
    Computer guess at user board
    """
    print("Now the computer's turn!")
    guess_col = random_num(comp)
    guess_row = random_num(comp)
    print(f"They've chosen {guess_col}, {guess_row}")
    if user[guess_col][guess_row] == " o ":
        user[guess_col][guess_row] = " # "
        print("It's a hit! :(")
    else:
        user[guess_col][guess_row] = " * "
        print("YAY! They missed!")
    print("Here's your board: ")
    print_board(user)


def game_play():
    for i in range (0, 5):
        print(f"This is turn {i +1}/10")
        user_guess()
        comp_guess()
        i += 1



main()
welcome()
game_play()