import heapq

def check_goal(curr, goal):
    return curr == goal


def encode(curr):
    return f"{curr[0]}{curr[1]}"


def is_valid(x, y, size, river):
    return 0 <= x < size and 0 <= y < size and river[x][y] == 0


def h_value(curr, goal):
    x, y = curr
    x1, y1 = goal
    return abs(x - x1) + abs(y - y1)


def gen_move(s, size, river):
    row, col = s
    moves = [
        (1, 0), (0, 1), (1, 1),
        (-1, 0), (-1, 1), (-1, -1),
        (0, -1), (1, -1)
    ]
    children = []
    for dx, dy in moves:
        nx, ny = row + dx, col + dy
        if is_valid(nx, ny, size, river):
            children.append([nx, ny])
    return children


def reconstruct_path(parent, goal_key, um, size, river, initial, goal):
    path = []
    curr = goal_key
    while curr != "0":
        path.append(um[curr])
        curr = parent[curr]
    path.reverse()

    grid = [["." for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if river[i][j] == 1:
                grid[i][j] = "#"

    grid[initial[0]][initial[1]] = "i"
    grid[goal[0]][goal[1]] = "f"

    for (x, y) in path[1:-1]:
        grid[x][y] = "*"

    print("\nPath Matrix:")
    for i in range(size):
        print(" ".join(grid[i]))

    print("\nPath found:")
    for (x, y) in path:
        print(f"({x},{y})", end=" ")
    print()


def solve(initial, goal, size, river):
    pq = []
    parent = {}
    um = {}
    g_cost = {}
    closed = set()

    start_key = encode(initial)
    um[start_key] = initial
    parent[start_key] = "0"
    g_cost[start_key] = 0
    heapq.heappush(pq, (h_value(initial, goal), 0.0, start_key))

    while pq:
        f, g, key = heapq.heappop(pq)
        curr_pos = um[key]

        if check_goal(curr_pos, goal):
            reconstruct_path(parent, key, um, size, river, initial, goal)
            return

        if key in closed:
            continue
        closed.add(key)

        for child in gen_move(curr_pos, size, river):
            child_key = encode(child)
            step_cost = 1.5 if (child[0] != curr_pos[0] and child[1] != curr_pos[1]) else 1.0
            new_g = g_cost[key] + step_cost
            f_new = new_g + h_value(child, goal)

            if child_key not in g_cost or new_g < g_cost[child_key]:
                g_cost[child_key] = new_g
                parent[child_key] = key
                um[child_key] = child
                heapq.heappush(pq, (f_new, new_g, child_key))

    print("No path found.")


def main():
    size = int(input("Enter size of matrix: "))
    river = [[0 for _ in range(size)] for _ in range(size)]

    x, y = map(int, input("Enter coordinates of initial position (indexed from 0): ").split())
    initial = [x, y]

    x, y = map(int, input("Enter coordinates of goal position (indexed from 0): ").split())
    goal = [x, y]

    size_r = int(input("Enter size of river: "))
    print("Enter points of river:")
    for i in range(size_r):
        x, y = map(int, input(f"Point {i + 1}: ").split())
        river[x][y] = 1

    solve(initial, goal, size, river)


if __name__ == "__main__":
    main()
