import os
import random

def initialize_board():
    return [' ' for _ in range(10)]

def print_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def is_board_full(board):
    return board.count(' ') == 1

def is_winner(board, letter):
    return (
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        (board[1] == letter and board[4] == letter and board[7] == letter) or
        (board[2] == letter and board[5] == letter and board[8] == letter) or
        (board[3] == letter and board[6] == letter and board[9] == letter) or
        (board[1] == letter and board[5] == letter and board[9] == letter) or
        (board[3] == letter and board[5] == letter and board[7] == letter)
    )

def player_move(board):
    while True:
        move = input("Please select a position to enter the X between 1 to 9: ")
        try:
            move = int(move)
            if 1 <= move <= 9 and board[move] == ' ':
                return move
            else:
                print('Sorry, this position is invalid or already occupied.')
        except ValueError:
            print('Please enter a valid number.')

def computer_move(board):
    possible_moves = [x for x in range(1, 10) if board[x] == ' ']
    if not possible_moves:
        return None  # No available moves
    for letter in ['O', 'X']:
        for move in possible_moves:
            boardcopy = board[:]
            boardcopy[move] = letter
            if is_winner(boardcopy, letter):
                return move
    return random.choice(possible_moves) if possible_moves else None

def start_game():
    print("Welcome to the game!")
    score_count = 0
    while True:
        board = initialize_board()
        print_board(board)

        while not is_board_full(board):
            move = player_move(board)
            board[move] = 'X'
            os.system('clear' if os.name == 'posix' else 'cls')
            print_board(board)

            if is_winner(board, 'X'):
                score_count += 1
                print(f"You win! Your score is {score_count}")
                break

            move = computer_move(board)
            if move is None:
                break
            board[move] = 'O'
            os.system('clear' if os.name == 'posix' else 'cls')
            print_board(board)

            if is_winner(board, 'O'):
                score_count -= 1
                print(f"Sorry, you lose 😢! Your score is {score_count}")
                break

        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again != 'y':
            print("It's nice playing with you!")
            break

start_game()
