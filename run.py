# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Need: complete winning checking
# Need: dont show the boards again at cycle 10 but show a winning statement

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
    ship_spot = 0
    while ship_spot < 4:
        ship_spot = 0
        #reset ship_spot value every loop
        ship_col = random_num(board)
        ship_row = random_num(board)
        board[ship_col][ship_row] = " o "
        for list in board:
            ship_spot += list.count(" o ")


def welcome():
    """
    Opening message to the game
    """
    print("Welcome to you vs. computer Battleships!")
    username = input("Type in a username and press return: ")
    print(f'''Hi {username}! We will auto generate your battleship locations.
You have 4 battleships to find within the computer's board.''')
    print("Here is the computer's board:")
    print_board(user_guesses)


def generate_boards():
    """
    Creates all the boards ready for use. A user board which will house the
    user's battleships that the computer will try to find. The comp board is
    the computer board housing the computer's battleships but the user_guesses
    board will be the version of the computer board shown to the user - we
    don't want to show the user where the computer's ships are!
    """
    make_board(user)
    make_board(comp)
    make_board(user_guesses)
    generate_ship_loc(user)
    generate_ship_loc(comp)


def user_guess():
    """
    Get user input on battleship guess, check whether it is valid data,
    check whether that shot has already been taken, check whether they hit a
    battleship and show them the result of their turn.
    """
    print("Here is the computer's board:")
    print_board(user_guesses)
    repeat = True
    while repeat:

        while True:
            print("Which column would you like to fire at?")
            guess_col = input("Enter a number and press enter: ")
            if validate_data(guess_col):
                break
        while True:
            print("Which row would you like to fire at?")
            guess_row = input("Enter a number and press enter: ")
            if validate_data(guess_row):
                break

        guess_col = int(guess_col)
        guess_row = int(guess_row)

        if (user_guesses[guess_col][guess_row] == " * "
                or user_guesses[guess_col][guess_row] == " # "):
            print("You've already picked that spot, try again!")
        else:
            repeat = False

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
    repeat = True

    guess_col = random_num(comp)
    guess_row = random_num(comp)

    while repeat:
        if (user[guess_col][guess_row] == " * "
                or user[guess_col][guess_row] == " # "):
            guess_col = random_num(comp)
            guess_row = random_num(comp)
        else:
            repeat = False

    print(f"They've chosen {guess_col}, {guess_row}")
    if user[guess_col][guess_row] == " o ":
        user[guess_col][guess_row] = " # "
        print("It's a hit! :(")
    else:
        user[guess_col][guess_row] = " * "
        print("YAY! They missed!")
    print("Here's your board: ")
    print_board(user)
    check_winner(user)


def game_play():
    for i in range(0, 10):
        print(f"This is turn {i +1}/10")
        user_guess()
        comp_guess()
        i += 1


def validate_data(value):
    """
    If values is not between 0 and 4, will raise an error and request a new
    input
    """
    try:
        if int(value) > 4 or int(value) < 0:
            raise ValueError(
                "Your shot is out of bounds! Choose a number between 0 and 4"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        return False

    return True


def check_winner(board):
    """
    Sums the number of times " o " (battleships) appear in the board. if it is
    equal to zero, that means someone has won.
    """
    total = 0
    for list in board:
        total += list.count(" o ")
    if total == 0:
        print("The game is WON!")


generate_boards()
welcome()
game_play()
