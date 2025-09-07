import math

USER = 'X'
AI = 'O'
EMPTY = ' '


def print_board(b):
    print("\nBoard:")
    for r in range(3):
        print(" ", end="")
        for c in range(3):
            i = r * 3 + c
            cell = str(i + 1) if b[i] == EMPTY else b[i]
            print(cell, end="")
            if c < 2:
                print(" | ", end="")
        print()
        if r < 2:
            print("---+---+---")
    print()


def check_winner(b):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for w in wins:
        if b[w[0]] != EMPTY and b[w[0]] == b[w[1]] == b[w[2]]:
            return -1 if b[w[0]] == AI else 1
    return 0


def moves_left(b):
    return EMPTY in b


def minimax(b, player_ai):
    score = check_winner(b)
    if score == 1 or score == -1:
        return score
    if not moves_left(b):
        return 0

    if player_ai:
        best = 1000
        for i in range(9):
            if b[i] == EMPTY:
                b[i] = AI
                best = min(best, minimax(b, False))
                b[i] = EMPTY
        return best
    else:
        best = -1000
        for i in range(9):
            if b[i] == EMPTY:
                b[i] = USER
                best = max(best, minimax(b, True))
                b[i] = EMPTY
        return best


def find_move(b):
    best_val = 1000
    best_move = -1

    for i in range(9):
        if b[i] == EMPTY:
            b[i] = AI
            move_val = minimax(b, False)
            b[i] = EMPTY
            if move_val < best_val:
                best_move = i
                best_val = move_val
    return best_move


def main():
    board = [EMPTY] * 9
    print("Tic Tac Toe (User = X, Computer = O)")
    print_board(board)

    while True:
        try:
            user_move = int(input("Enter your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")
            continue

        if user_move < 0 or user_move > 8 or board[user_move] != EMPTY:
            print("Invalid Move! Try again.")
            continue

        board[user_move] = USER
        print_board(board)

        if check_winner(board) == 1:
            print("You win!")
            break
        if not moves_left(board):
            print("It's a Draw!")
            break

        move_ai = find_move(board)
        board[move_ai] = AI
        print(f"Computer chooses position {move_ai + 1}")
        print_board(board)

        if check_winner(board) == -1:
            print("Computer Wins!")
            break
        if not moves_left(board):
            print("It's a Draw!")
            break


if __name__ == "__main__":
    main()
