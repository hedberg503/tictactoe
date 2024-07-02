# TicTacToe
#######################################
# Print the blank Tic Tac Tow board
# Take in player input
# Place the input on the board
# Check if the game is won, tied, lost, continues
# Rinse and repeat until the game is won or tied
# Ask if players want to play again
#######################################

from IPython.display import clear_output
import random

def display_board(board):
    '''
    OUTPUT: Tic Tac Toe board
    '''
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

def choose_player_input():
    '''
    OUTPUT: (player1marker, player2marker)
    '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()
        if marker == 'X':
            return('X','O')
        elif marker == 'O':
            return('O','X')
        else:
            continue

def place_marker(board, marker, position):
    '''
    Change the marker in the listed position
    '''
    board[position] = marker

def check_win(board, mark):
    '''
    Possible winning combinations:
    All Rows
    All Columns
    Two diagonals
    OUTPUT: True or False
    '''
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[7] == board[5] == board[3] == mark))

def choose_first_player():
    '''
    OUTPUT: Name of Player who goes first
    '''
    coin_flip = random.randint(0,1)
    if coin_flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def check_valid_space(board, position):
    '''
    OUTPUT: True or False
    '''
    return board[position] == ' '

def check_full_board(board):
    '''
    OUTPUT: True or False
    If there are valid spaces left we return False
    '''
    for i in range(1,10):
        if check_valid_space(board,i):
            return False
    return True

def player_space_choice(board):
    '''
    OUTPUT: integer of position to change marker
    Ask the user for position input and check if it is a valid space
    '''
    position = 0
    while position not in range(1,10) or not check_valid_space(board, position):
        position = int(input('Choose a position: (1-9) '))
    return position

def replay():
    choice = input("Play again? Enter Y or N").upper()
    return choice == 'Y'
    
print('Welcome to Tic Tac Toe!')
print('The board is setup as follows:')
print('1|2|3')
print('4|5|6')
print('7|8|9')
print('The computer will randomly choose which player goes first.')

while True:
    #SETUP
    board = [' ']*10
    player1marker, player2marker = choose_player_input()

    turn = choose_first_player()
    print(turn + ' will go first.')

    play_game = input('Ready to play? Y or N').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_space_choice(board)
            place_marker(board,player1marker,position)
            if check_win(board,player1marker):
                display_board(board)
                print('Player 1 Wins!')
                game_on = False
            else:
                if check_full_board(board):
                    display_board(board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(board)
            position = player_space_choice(board)
            place_marker(board,player2marker,position)
            if check_win(board,player2marker):
                display_board(board)
                print('Player 2 Wins!')
                game_on = False
            else:
                if check_full_board(board):
                    display_board(board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 1'
    
    if not replay():
        break


