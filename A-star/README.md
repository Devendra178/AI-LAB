# River Crossing Pathfinding: A* Algorithm

## Problem Statement

The **River Crossing Problem** involves finding the optimal path from an initial position to a goal position on an N×N grid while avoiding river obstacles. The grid contains:
- **Traversable cells** (represented as `0`)
- **River cells** (obstacles represented as `1`)

The objective is to navigate from the starting point to the destination using the **A* search algorithm**, which combines:
- **g(n)**: Actual cost from start to current node
- **h(n)**: Heuristic estimate (Manhattan distance) from current node to goal

**Movement Rules:**
- **Orthogonal moves** (up, down, left, right): Cost = 1.0
- **Diagonal moves** (northeast, southeast, southwest, northwest): Cost = 1.5

## Goal State

Navigate from initial position `(x_i, y_i)` to goal position `(x_g, y_g)` while:
- Avoiding river cells
- Minimizing total path cost
- Finding the optimal (shortest/cheapest) path

## Objectives

1. Implement **A* search algorithm** for pathfinding with obstacles
2. Use **Manhattan distance** as an admissible heuristic
3. Handle **diagonal movement** with different step costs
4. Visualize the solution path on the grid
5. Understand informed search in AI

## Algorithm: A* Search

### Overview

A* is an informed search algorithm that uses:
- **f(n) = g(n) + h(n)**
  - **g(n)**: Actual cost from start to node n
  - **h(n)**: Heuristic estimate from n to goal (Manhattan distance)

### Why A*?

- **Complete**: Always finds a solution if one exists
- **Optimal**: Finds the least-cost path (when heuristic is admissible)
- **Efficient**: Explores fewer nodes than uninformed search (BFS/DFS)
- **Goal-directed**: Uses heuristic to guide search toward the goal

### Heuristic Function

**Manhattan Distance** (L1 distance):
```
h(n) = |x_current - x_goal| + |y_current - y_goal|
```

This heuristic is:
- **Admissible**: Never overestimates the actual cost
- **Consistent**: Satisfies triangle inequality
- **Efficient**: Simple to compute

### Pseudocode

```
Initialize:
    priority_queue pq
    g_cost[start] = 0
    parent[start] = NULL
    f_start = g_cost[start] + h(start, goal)
    pq.push((f_start, g_start, start))
    closed_set = {}

While pq not empty:
    (f, g, current) = pq.pop()
    
    If current == goal:
        reconstruct_path()
        return SUCCESS
    
    If current in closed_set:
        continue
    
    closed_set.add(current)
    
    For each neighbor of current:
        If neighbor is valid and not river:
            step_cost = 1.5 if diagonal else 1.0
            new_g = g_cost[current] + step_cost
            
            If neighbor not visited OR new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_new = new_g + h(neighbor, goal)
                parent[neighbor] = current
                pq.push((f_new, new_g, neighbor))

If pq empty:
    return NO_PATH
```

## State Representation

- **Grid**: `river[N][N]` where:
  - `0` = traversable cell
  - `1` = river (obstacle)
- **State**: `[x, y]` coordinates
- **Encoding**: States encoded as strings `"xy"` for fast lookup

## Move Generation

From any position `(x, y)`, generate up to **8 possible moves**:

| Direction | Delta | Cost |
|-----------|-------|------|
| Right     | (0, +1) | 1.0 |
| Left      | (0, -1) | 1.0 |
| Down      | (+1, 0) | 1.0 |
| Up        | (-1, 0) | 1.0 |
| Down-Right | (+1, +1) | 1.5 |
| Down-Left  | (+1, -1) | 1.5 |
| Up-Right   | (-1, +1) | 1.5 |
| Up-Left    | (-1, -1) | 1.5 |

**Validation**: Each move is checked for:
- Grid boundaries: `0 <= x < N and 0 <= y < N`
- Obstacle avoidance: `river[x][y] == 0`

## Data Structures Used

| Purpose | Data Structure | Reason |
|---------|---------------|--------|
| Priority queue | `heapq` (min-heap) | Efficient extraction of minimum f-cost node |
| Visited states | `set` | O(1) lookup for closed set |
| Parent mapping | `dict` | Path reconstruction |
| State encoding | `dict` (um) | Map encoded keys to coordinates |
| Cost tracking | `dict` (g_cost) | Store actual cost to each node |

## Complexity Analysis

Let:
- **N** = grid size (N×N)
- **E** = number of edges ≈ 8N² (8 neighbors per cell)
- **V** = number of vertices = N²

| Aspect | Complexity | Notes |
|--------|-----------|-------|
| **Time Complexity** | O(E log V) = O(N² log N²) | Priority queue operations |
| **Space Complexity** | O(V) = O(N²) | Storing g_cost, parent, closed set |
| **Worst Case** | O(N² log N²) | When all cells are explored |
| **Best Case** | O(d log d) | Direct path with depth d |

### Comparison with Other Algorithms

| Algorithm | Time | Space | Optimal | Heuristic |
|-----------|------|-------|---------|-----------|
| **DFS** | O(b^d) | O(bd) | ❌ No | ❌ Blind |
| **BFS** | O(b^d) | O(b^d) | ✅ Yes | ❌ Blind |
| **Greedy** | O(b·log b × d) | O(b^d) | ❌ No | ✅ Yes |
| **A*** | O(E log V) | O(V) | ✅ Yes | ✅ Yes |

## Output Visualization

The program outputs:

### 1. Path Matrix
Grid visualization with:
- `.` = empty traversable cell
- `#` = river (obstacle)
- `i` = initial position
- `f` = final/goal position
- `*` = path cells

### 2. Path Coordinates
Sequence of `(x, y)` coordinates from start to goal

### Example Output

```
Path Matrix:
i . . . #
* * . . #
. * * . #
. . * * f
. . . . .

Path found:
(0,0) (1,0) (1,1) (2,1) (2,2) (3,2) (3,3) (3,4)
```

## How to Run

### Prerequisites
- Python 3.x
- No external libraries required (uses standard library)

### Execution

```bash
python river_crossing.py
```

### Sample Input

```
Enter size of matrix: 5
Enter coordinates of initial position (indexed from 0): 0 0
Enter coordinates of goal position (indexed from 0): 4 4
Enter size of river: 3
Enter points of river:
Point 1: 0 4
Point 2: 1 4
Point 3: 2 4
```

### Sample Output

```
Path Matrix:
i . . . #
* * . . #
. * * . #
. . * * .
. . . * f

Path found:
(0,0) (1,0) (1,1) (2,1) (2,2) (3,2) (3,3) (4,3) (4,4)
```

## Key Features

✅ **Optimal Pathfinding**: Finds the shortest/cheapest path  
✅ **Diagonal Movement**: Supports 8-directional movement with appropriate costs  
✅ **Obstacle Avoidance**: Navigates around river cells  
✅ **Visual Output**: Clear grid representation of the solution  
✅ **Efficient Search**: Uses A* with admissible heuristic  
✅ **Complete Solution**: Guarantees finding a path if one exists  

## Algorithm Advantages

1. **Optimality**: Manhattan distance is admissible → guaranteed optimal path
2. **Efficiency**: Explores fewer nodes than BFS by using heuristic guidance
3. **Completeness**: Always finds a solution if one exists
4. **Flexibility**: Easy to modify for different heuristics or movement costs