def print_board(board):
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])


def turn_token(count):
    if count % 2 == 0:
        return "O"
    else:
        return "X"


def ask_move(count, board):
    player = turn_token(count)
    print_board(board)
    print("It is your move " + player + ":")
    move = int(input("What is your move: "))
    valid_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if move in valid_moves:
        if board[move] == " ":
            print("You selected " + str(move))
            board[move] = player
            return board
        else:
            print("Try Again")
            return ask_move(count, board)
    else:
        print("Try Again")
        return ask_move(count, board)


def check_win(board):
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
    if " " in board.values():
        pass
    else:
        return True


def game():
    game_board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    count = 0
    play = True
    while play:
        player = turn_token(count)
        ask_move(count, game_board)
        if check_win(game_board):
            print(player + " WON!!!!!")
            play = False
        elif check_cats(game_board):
            print("Everybody Loses")
            play = False
        count += 1
    again = input("Do you want to play again? y or n")
    if again == "y":
        game()
    else:
        exit()


if __name__ == '__main__':
    game()
