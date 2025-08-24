import time
import copy


def heuristic(curr, goal):
    """Count misplaced tiles compared to the goal."""
    d = 0
    for i in range(len(curr)):
        for j in range(len(curr[i])):
            if curr[i][j] != goal[i][j]:
                d += 1
    return d


def find_pos(board):
    """Find position of the blank tile (0)."""
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return (-1, -1)


def compare(a, b):
    return a == b


def up(board):
    """Move blank tile up."""
    s = copy.deepcopy(board)
    row, col = find_pos(s)
    if row > 0:
        s[row][col], s[row - 1][col] = s[row - 1][col], s[row][col]
    return s


def down(board):
    """Move blank tile down."""
    s = copy.deepcopy(board)
    row, col = find_pos(s)
    if row < len(s) - 1:
        s[row][col], s[row + 1][col] = s[row + 1][col], s[row][col]
    return s


def left(board):
    """Move blank tile left."""
    s = copy.deepcopy(board)
    row, col = find_pos(s)
    if col > 0:
        s[row][col], s[row][col - 1] = s[row][col - 1], s[row][col]
    return s


def right(board):
    """Move blank tile right."""
    s = copy.deepcopy(board)
    row, col = find_pos(s)
    if col < len(s[0]) - 1:
        s[row][col], s[row][col + 1] = s[row][col + 1], s[row][col]
    return s


def search(start, goal):
    """Hill Climbing / Simple Heuristic-based Search."""
    q = [(heuristic(start, goal), start)]
    visited = []

    while q:
        q.sort(key=lambda x: x[0])  # Sort by heuristic
        hval, state = q.pop(0)

        if compare(state, goal):
            print("Found!")
            print("Visited states:", len(visited))
            return

        visited.append(state)

        # Generate possible moves
        children = [up(state), down(state), left(state), right(state)]

        for child in children:
            h = heuristic(child, goal)
            node = (h, child)

            # Skip if already visited or in queue
            if (child not in visited) and all(not compare(child, n[1]) for n in q):
                q.append(node)

        q.sort(key=lambda x: x[0])
        if q and q[0][0] > hval:
            print(f"Heuristic of child greater than parent: {q[0][0]} > {hval}")
            return

    print("Not Found.")


def main():
    s = [[1, 2, 3],
         [4, 5, 6],
         [8, 7, 0]]
    g = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]]

    start_time = time.time()
    search(s, g)
    end_time = time.time()

    duration = (end_time - start_time) * 1000  # milliseconds
    print(f"Execution time: {duration:.2f} ms")


if __name__ == "__main__":
    main()
