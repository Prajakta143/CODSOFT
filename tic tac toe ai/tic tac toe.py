import math

board = [" " for _ in range(9)]

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def full():
    return " " not in board

def minimax(is_ai):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if full():
        return 0

    if is_ai:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best

def ai_turn():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def player_turn():
    pos = int(input("Enter position (1-9): ")) - 1
    if board[pos] == " ":
        board[pos] = "X"
    else:
        print("Spot taken, try again")
        player_turn()

print("Tic Tac Toe – You (X) vs AI (O)")

while True:
    show_board()
    player_turn()
    if winner("X"):
        show_board()
        print("You win ")
        break
    if full():
        show_board()
        print("Draw ")
        break

    ai_turn()
    if winner("O"):
        show_board()
        print("AI wins ")
        break
    if full():
        show_board()
        print("Draw ")
        break
