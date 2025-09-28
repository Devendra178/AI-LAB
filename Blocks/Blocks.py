from copy import deepcopy

class State:
    def __init__(self):
        self.on = []       # list of (block, on_what)
        self.moves = []    # list of moves made so far


def is_goal(state, goal):
    """Check if current state matches the goal configuration."""
    for block, target in goal:
        found = False
        for b, t in state.on:
            if b == block and t == target:
                found = True
                break
        if not found:
            return False
    return True


def get_clear_blocks(state):
    """Return list of blocks that have nothing on top."""
    all_blocks = [b for b, _ in state.on]
    has_something_on_top = []

    for b, on in state.on:
        if on != "Table":
            has_something_on_top.append(on[0])

    clear = [b for b in all_blocks if b not in has_something_on_top]
    return clear


def children(current):
    """Generate all possible next states."""
    next_states = []
    clear_blocks = get_clear_blocks(current)

    for x in clear_blocks:
        # Find what block x is on
        under = ""
        for b, on in current.on:
            if b == x:
                under = on
                break

        # Move x to table if not already there
        if under != "Table":
            new_state = deepcopy(current)
            for i, (b, on) in enumerate(new_state.on):
                if b == x:
                    new_state.on[i] = (b, "Table")
                    break
            move = f"Move {x} to Table"
            new_state.moves.append(move)
            next_states.append(new_state)

        # Move x onto another clear block y
        for y in clear_blocks:
            if y == x:
                continue
            new_state = deepcopy(current)
            for i, (b, on) in enumerate(new_state.on):
                if b == x:
                    new_state.on[i] = (b, y)
                    break
            move = f"Move {x} onto {y}"
            new_state.moves.append(move)
            next_states.append(new_state)

    return next_states


def dfs(start, goal, depth_limit):
    """Depth-limited DFS for block world."""
    stack = [start]

    while stack:
        current = stack.pop()

        if is_goal(current, goal):
            print("\nGoal reached!\nSequence of moves:")
            for move in current.moves:
                print(move)
            return True

        if len(current.moves) < depth_limit:
            for next_state in children(current):
                stack.append(next_state)

    return False


# -------------------- MAIN --------------------

def main():
    n = int(input("Enter number of blocks: "))
    start = State()
    goal = []

    print("\nEnter start state (format: Block On):")
    for _ in range(n):
        block, on = input().split()
        start.on.append((block, on))

    print("\nEnter goal state (format: Block On):")
    for _ in range(n):
        block, on = input().split()
        goal.append((block, on))

    depth_limit = int(input("\nEnter depth limit: "))

    if not dfs(start, goal, depth_limit):
        print("Goal not found within depth limit.")


if __name__ == "__main__":
    main()
