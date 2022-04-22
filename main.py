import csv
import os.path
from random import randrange


def read_move_tables():
    #function to read the list of games won and lost to select moves
    file_exists = os.path.exists('ai_tables.csv')
    moves = dict()
    if file_exists:
        with open('ai_tables.csv', mode='r') as infile:
            reader = csv.reader(infile)
            moves = {rows[0]: rows[1] for rows in reader}
            return moves
    else:
        return moves


def write_move_tables(moves):
    #write the moves to a file after each game ends
    a_file = open("ai_tables.csv", "w")
    writer = csv.writer(a_file)
    for key, value in moves.items():
        writer.writerow([key, value])
    a_file.close()


def print_board(board):
    #this fuction prints the board before/after each turn
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])


def turn_token(count):
    #this function just makes sure the turn switches
    if count % 2 == 0:
        return "O"
    else:
        return "X"


def ai_move(count, board, moves, log):
    player = turn_token(count)
    #this function for the AI's move
    if player == "O":
        move = randrange(1, 10, 1)
        rank = .5
        for history in moves.keys():
            histring = history
            if histring[0:len(log)] == log:
                if float(moves[history]) > rank:
                    if len(histring) == (len(log) + 1):
                        move = int(histring[len(log)])
                        rank = float(moves[history])
                        print(histring)
                        print(move)
                        print(rank)
        if board[move] == " ":
            return move
        else:
            return ai_move(count, board, moves, log)
    else:
        move = randrange(1, 10, 1)
        if board[move] == " ":
            return move
        else:
            return ai_move(count, board, moves, log)


def ask_move(count, board, moves, log):
    #this function asks for player move or calls function for ai move
    player = turn_token(count)
    print_board(board)
    print("It is your move " + player + ":")
    if player == "X":
        move = int(input("What is your move: "))
        valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if move in valid_moves:
            if board[move] == " ":
                print("You selected " + str(move))
                board[move] = player
                return move
            else:
                print("Try Again")
                return ask_move(count, board, moves, log)
        else:
            print("Try Again")
            return ask_move(count, board, moves, log)
    else:
        move = ai_move(count, board, moves, log)
        print("Computer chooses " + str(move))
        board[move] = player
        return move


def check_win(board):
    #this function checks if there is a winner
    if board[1] == board[2] and board[1] == board[3]:
        if board[1] != " ":
            return True
    if board[1] == board[5] and board[1] == board[9]:
        if board[1] != " ":
            return True
    if board[1] == board[4] and board[1] == board[7]:
        if board[1] != " ":
            return True
    if board[2] == board[5] and board[2] == board[8]:
        if board[2] != " ":
            return True
    if board[3] == board[5] and board[3] == board[7]:
        if board[3] != " ":
            return True
    if board[3] == board[6] and board[3] == board[9]:
        if board[3] != " ":
            return True
    if board[4] == board[5] and board[4] == board[6]:
        if board[4] != " ":
            return True
    if board[7] == board[8] and board[7] == board[9]:
        if board[7] != " ":
            return True


def check_cats(board):
    #this function checks for a cat's game
    if " " in board.values():
        pass
    else:
        return True


def game():
    #main game function
    game_board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    count = 0
    moves = read_move_tables()
    log = ""
    logs = list()
    play = True
    while play == True:
        player = turn_token(count)
        move = ask_move(count, game_board, moves, log)
        log = log + str(move)
        if len(log) > 1:
            logs.append(log)
        if check_win(game_board):
            print_board(game_board)
            print(player + " WON!!!!!")
            for in_log in logs:
                if in_log in moves:
                    if player == "O":
                        moves[in_log] = float(moves[in_log]) * 1.5
                    if player == "X":
                        moves[in_log] = float(moves[in_log]) * 0.5
                else:
                    if player == "O":
                        moves[in_log] = 1
                    if player == "X":
                        moves[in_log] = 0.1
            write_move_tables(moves)
            play = False
        elif check_cats(game_board):
            print_board(game_board)
            print("Everybody Loses")
            for in_log in logs:
                if in_log in moves:
                    if player == "O":
                        moves[in_log] = float(moves[in_log]) * 1.1
                    if player == "X":
                        moves[in_log] = float(moves[in_log]) * 0.75
                else:
                    moves[in_log] = 0.5
            write_move_tables(moves)
            play = False
        count += 1
    again = input("Do you want to play again? y or n")
    if again == "y":
        game()
    else:
        exit()


if __name__ == '__main__':
    game()
