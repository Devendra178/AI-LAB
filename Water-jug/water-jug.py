def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def fill_x(state):
    state['amount_x'] = state['x']

def fill_y(state):
    state['amount_y'] = state['y']

def empty_x(state):
    state['amount_x'] = 0

def empty_y(state):
    state['amount_y'] = 0

def pour_x_to_y(state):
    pour = min(state['amount_x'], state['y'] - state['amount_y'])
    state['amount_x'] -= pour
    state['amount_y'] += pour

def pour_y_to_x(state):
    pour = min(state['amount_y'], state['x'] - state['amount_x'])
    state['amount_y'] -= pour
    state['amount_x'] += pour

def reached_goal(state, goal):
    return (state['amount_x'] == goal) or (state['amount_y'] == goal)

def solve_jugs(state, goal):
    state['amount_x'] = 0
    state['amount_y'] = 0

    while not reached_goal(state, goal):
        if state['amount_x'] == 0:
            fill_x(state)
        elif state['amount_y'] == state['y']:
            empty_y(state)
        else:
            pour_x_to_y(state)
        print(f"({state['amount_x']}, {state['amount_y']})")

def main():
    state_name = input("Enter starting state (optional): ").strip()

    x = int(input("Enter capacity of jug x: "))
    y = int(input("Enter capacity of jug y: "))
    goal = int(input("Enter goal volume: "))

    a, b = x, y
    while b != 0:
        temp = b
        b = a % b
        a = temp
    gcd_val = a

    if goal > max(x, y) or (goal % gcd_val != 0):
        print("Goal not achievable with given jug sizes.")
        return

    state = {
        'x': x,
        'y': y,
        'amount_x': 0,
        'amount_y': 0
    }

    print("Starting state:")
    print(f"({state['amount_x']}, {state['amount_y']})")

    # If a state name was provided, you can label output (optional)
    if state_name:
        print(f"State label: {state_name}")

    solve_jugs(state, goal)

    print(f"Goal {goal} reached.")

if __name__ == "__main__":
    main()
