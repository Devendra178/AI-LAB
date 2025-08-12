def gen_move(s):
    row, col = 0, 0
    states = []
    # Find the position of 0 (empty tile)
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                row = i
                col = j
                break
    # Move up
    if row - 1 >= 0:
        temp = [r[:] for r in s]
        temp[row][col], temp[row-1][col] = temp[row-1][col], temp[row][col]
        states.append(temp)
    # Move down
    if row + 1 <= 2:
        temp = [r[:] for r in s]
        temp[row][col], temp[row+1][col] = temp[row+1][col], temp[row][col]
        states.append(temp)
    # Move left
    if col - 1 >= 0:
        temp = [r[:] for r in s]
        temp[row][col], temp[row][col-1] = temp[row][col-1], temp[row][col]
        states.append(temp)
    # Move right
    if col + 1 <= 2:
        temp = [r[:] for r in s]
        temp[row][col], temp[row][col+1] = temp[row][col+1], temp[row][col]
        states.append(temp)
    return states

def encode(s):
    key = ""
    for r in s:
        for x in r:
            key += str(x)
    return key

def solve(initial_state):
    goal_state = [[1,2,3],[4,5,6],[7,8,0]]
    stack = []
    visited = set()
    stack.append(initial_state)
    while stack:
        curr = stack.pop()
        visited.add(encode(curr))
        if curr == goal_state:
            print("Success")
            return
        states = gen_move(curr)
        for state in states:
            key = encode(state)
            if key not in visited:
                stack.append(state)
    print("No solution")

if __name__ == "__main__":
    print("Enter the initial state row by row (use 0 for the empty tile, separate numbers with spaces):")
    state = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").strip().split()))
        if len(row) != 3:
            print("Each row must have exactly 3 numbers.")
            exit(1)
        state.append(row)
    solve(state)
