import heapq

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

def h_value(s):
    goal_state = [[1,2,3],[4,5,6],[7,8,0]]
    count = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != goal_state[i][j]:
                count += 1
    return count

def solve(s):
    # Min-heap priority queue with elements as tuples (h_value, state_key)
    pq = []
    um = {}
    parent = {}
    visited = set()

    start_key = encode(s)
    um[start_key] = s
    parent[start_key] = "0"
    heapq.heappush(pq, (h_value(s), start_key))

    while pq:
        h, key = heapq.heappop(pq)

        if key in visited:
            continue
        visited.add(key)

        curr = um[key]

        print(f"h={h}")
        for row in curr:
            print(" ".join(map(str, row)))
        print("------")

        if h == 0:
            print("Goal reached!")
            return

        for next_state in gen_move(curr):
            next_key = encode(next_state)
            if next_key not in visited:
                um[next_key] = next_state
                parent[next_key] = key
                heapq.heappush(pq, (h_value(next_state), next_key))

if __name__ == "__main__":
    print("Enter the initial state row by row (use 0 for the empty tile, separate numbers with spaces):")
    state = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").strip().split()))
        if len(row) != 3:
            print("Each row must have exactly 3 numbers.")
            exit(1)
        state.append(row)
    print("\nInitial state:")
    for row in state:
        print(" ".join(map(str, row)))
    print()
    solve(state)
