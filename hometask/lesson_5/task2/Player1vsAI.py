import random
print("Добро пожаловать в 'Крестики-нолики'! (Против AI)\n")
def draw_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

def check_draw(board):
    if " " not in board:
        return True
    return False

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    return False

def play_game():
    player1 = input("Имя игрока 1: ")
    player2 = ("AI")
    players = [player1, player2]
    random.shuffle(players)
    print(players[0] + " будет X и " + players[1] + " будет О.")
    board = [" " for x in range(9)]
    while True:
        for player in players:
            if player == player2:
                empty_spaces = [i for i, x in enumerate(board) if x == " "]
                for move in empty_spaces:
                    board[move] = "O"
                    if check_win(board, "O"):
                        print("AI выбирает клетку", move + 1)
                        break
                    else:
                        board[move] = " "
                else:
                    for move in empty_spaces:
                        board[move] = "X"
                        if check_win(board, "X"):
                            board[move] = "O"
                            print("AI выбирает клетку", move + 1)
                            break
                        else:
                            board[move] = " "
                    else:
                        move = random.choice(empty_spaces)
                        board[move] = "O"
                        print("AI выбирает клетку", move + 1)
            else:
                print(player + " ходит.")
                draw_board(board)
                move = int(input("Выберите свой ход (1-9): ")) - 1
                while board[move] != " ":
                    print("Неправильный ход. Попробуйте ещё раз!")
                    move = int(input("Выберите свой ход (1-9): ")) - 1
                board[move] = "X"
            if check_win(board, "X" if player == player1 else "O"):
                print(player + " выиграл!")
                return
            if check_draw(board):
                print("Это ничья!")
                return
play_game()
