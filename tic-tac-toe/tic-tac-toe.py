magic = [8,1,6,3,5,7,4,9,2]

def print_board(b):
    print("\nBoard:")
    for r in range(3):
        row_str = " "
        for c in range(3):
            i = r * 3 + c
            cell = str(i+1) if b[i] == ' ' else b[i]
            row_str += cell
            if c < 2:
                row_str += " | "
        print(row_str)
        if r < 2:
            print("---+---+---")
    print()

def check_win(b, p):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for line in wins:
        if b[line[0]] == p and b[line[1]] == p and b[line[2]] == p:
            return True
    return False

def collect_magic(board, player):
    nums = []
    for i in range(9):
        if board[i] == player:
            nums.append(magic[i])
    return nums

def completes15(nums, cand):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] + cand == 15:
                return True
    return False

def computer_move(board):
    ai_nums = collect_magic(board, 'O')
    human_nums = collect_magic(board, 'X')
    # Win if possible
    for i in range(9):
        if board[i] == ' ' and completes15(ai_nums, magic[i]):
            return i
    # Block if necessary
    for i in range(9):
        if board[i] == ' ' and completes15(human_nums, magic[i]):
            return i
    # Take center if available
    if board[4] == ' ':
        return 4
    # Take a corner if available
    for idx in [0,2,6,8]:
        if board[idx] == ' ':
            return idx
    # Take a side if available
    for idx in [1,3,5,7]:
        if board[idx] == ' ':
            return idx
    # Fallback: first empty position
    for i in range(9):
        if board[i] == ' ':
            return i
    return -1

def main():
    board = [' '] * 9
    user_turn = True
    moves = 0

    print("Tic-Tac-Toe (Magic Square AI)")
    print("You are X, computer is O.")

    while True:
        print_board(board)
        if user_turn:
            print("User's turn")
            while True:
                try:
                    pos = int(input("Your move (1-9): "))
                    print(f" You entered: {pos}")
                except ValueError:
                    print("Invalid input, please enter a number between 1 and 9.")
                    continue
                if pos < 1 or pos > 9 or board[pos-1] != ' ':
                    print("Invalid move, try again.")
                    continue
                break
            board[pos-1] = 'X'
            moves += 1
            if check_win(board, 'X'):
                print_board(board)
                print("You WIN!")
                break
        else:
            print(" Computer's turn")
            cm = computer_move(board)
            print(f" Computer chooses index {cm} (pos {cm+1})")
            if cm == -1:
                break
            board[cm] = 'O'
            moves += 1
            if check_win(board, 'O'):
                print_board(board)
                print("Computer WINS.")
                break

        if moves >= 9:
            print_board(board)
            print("It's a draw.")
            break
        user_turn = not user_turn

    print("Game over.")

if __name__ == "__main__":
    main()
