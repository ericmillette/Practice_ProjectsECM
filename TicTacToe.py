
# plays a game of TicTacToe, player vs player
# Create a gameboard... Display gameboard
# create player and computer (X and O)
# moderate turns, wins, and ties

#GLOBAL VARIABLES --------------
board = "-" * 9
game_over = False
winner = None
current_player = "X"
# ------------------------------

def display_board(): # x is arbitrary counter
    x = 0
    for i in range(3):
        print(board[x] + " | " + board[x + 1] + " | " + board[x + 2])
        x += 3

def conduct_turn():
    global current_player
    print("It is " + current_player + "'s turn.") # asks for input
    position = input("Choose a position between 1 and 9: ")

    if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]: # rejects input if it's not 1-9
        position = input("Error. Choose a position between 1 and 9: ")

    position = int(position) - 1 # designates position selected to proper index
    board[position] == current_player

    if current_player == "X": # flip player from X to O, or vice versa
        current_player == "O"
    else:
        current_player == "X"

def check_win(): # checks if all "-" have been fulfilled
        check_rows()
        check_columns()
        check_diagonals()
        if winner == "X":
            print("The winner is X!")
        elif winner == "O":
            print("The winner is O!")
        else:
            print("It is a tie.")
        exit()

def check_rows(): # determines if a player has won by completing a row, otherwise a tie
    row_1 = board[0] + board[1] + board[2]
    row_2 = board[3] + board[4] + board[5]
    row_3 = board[6] + board[7] + board[8]

#    if row_1 != "---" or row_2 != "---" or row_3 != "---":
#        game_over == True
    if row_1 == "XXX" or row_2 == "XXX" or row_3 == "XXX":
        winner = "X"
    else:
        winner = "O"

def check_columns(): # determines if a player has won by completing a column
    column_1 = board[0] + board[3] + board[6]
    column_2 = board[1] + board[4] + board[7]
    column_3 = board[2] + board[5] + board[8]

#    if column_1 != "---" or column_2 != "---" or column_3 != "---":
#        game_over == True
    if column_1 == "XXX" or column_2 == "XXX" or column_3 == "XXX":
        winner = "X"
    else:
        winner = "O"

def check_diagonals(): # determines if a player has won by completing a diagonal
    diagonal_1 = board[0] + board[4] + board[8]
    diagonal_2 = board[2] + board[4] + board[6]

#    if diagonal_1 != "---" or diagonal_2 != "---":
#        game_over == True
    if diagonal_1 == "XXX" or diagonal_2 == "XXX":
        winner = "X"
    else:
        winner = "O"

def play_tictactoe():
    print("Let's play TicTacToe.")
    display_board()
    while not game_over:
        if "-" not in board:
            check_win()
        else:
            conduct_turn()

play_tictactoe()