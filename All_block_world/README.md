Block World Problem: Depth-Limited DFS

Problem Statement
The Block World Problem is a classic planning problem in AI where blocks are stacked on a table. The goal is to rearrange blocks from an initial configuration to a goal configuration using valid moves.


Constraints:

Only blocks with nothing on top can be moved (clear blocks)
A block can be moved to the table or onto another clear block
Find a sequence of moves to reach the goal state

Goal State
Transform the initial block arrangement into the target configuration by moving blocks one at a time.
Example:
Initial State:        Goal State:
  A                     C
  B                     B
  C                     A
-----                 -----
Table                 Table
Objectives

Implement Depth-Limited DFS for state space search
Generate all valid block movements
Track clear blocks (no block on top)
Find a sequence of moves to reach the goal
Handle depth constraints to avoid infinite search

Algorithm: Depth-Limited DFS
Overview
Depth-First Search (DFS) explores states by going as deep as possible before backtracking. The depth limit prevents infinite exploration.
Pseudocode
function dfs(start, goal, depth_limit):
    stack = [start]
    
    while stack not empty:
        current = stack.pop()
        
        if current matches goal:
            print moves
            return SUCCESS
        
        if depth(current) < depth_limit:
            for each valid move from current:
                generate new_state
                push new_state to stack
    
    return FAILURE
State Representation
State Structure:
pythonclass State:
    on = []      # List of (block, on_what) tuples
    moves = []   # Sequence of moves to reach this state

Example:
on = [('A', 'B'), ('B', 'C'), ('C', 'Table')]
Means: A is on B, B is on C, C is on Table
Move Generation
Valid Moves

Move block X to Table

Condition: X must be clear (nothing on top)
Action: Place X on table


Move block X onto block Y

Condition: Both X and Y must be clear
Action: Stack X on top of Y



Clear Block Detection
A block is clear if no other block is on top of it.
pythondef get_clear_blocks(state):
    # Find all blocks
    all_blocks = [b for b, _ in state.on]
    
    # Find blocks that have something on top
    has_on_top = [on for b, on in state.on if on != "Table"]
    
    # Clear blocks = all blocks - blocks with something on top
    clear = [b for b in all_blocks if b not in has_on_top]
    return clear
Complexity Analysis
Let:

b = branching factor (number of possible moves per state)
d = depth limit

AspectComplexityNotesTimeO(b^d)Explores up to b^d statesSpaceO(b×d)Stack stores current pathCompleteness❌ NoMay miss solution beyond depth limitOptimality❌ NoFinds first solution, not shortest
Comparison with Other Search Algorithms
AlgorithmTimeSpaceOptimalCompleteDFS (Depth-Limited)O(b^d)O(bd)❌ No⚠️ LimitedBFSO(b^d)O(b^d)✅ Yes✅ YesDFS (No Limit)O(b^∞)O(b×∞)❌ No❌ No
Sample Input/Output
Example 1: Simple Stack
Input:
Enter number of blocks: 3
Enter start state (format: Block On):
A B
B C
C Table
Enter goal state (format: Block On):
C B
B A
A Table
Enter depth limit: 10
Output:
Goal reached!
Sequence of moves:
Move A to Table
Move B to Table
Move C onto B
Move B onto A
Example 2: Already at Goal
Input:
Enter number of blocks: 2
Enter start state (format: Block On):
A B
B Table
Enter goal state (format: Block On):
A B
B Table
Enter depth limit: 5
Output:
Goal reached!
Sequence of moves:
(empty - no moves needed)
Example 3: Depth Limit Exceeded
Input:
Enter number of blocks: 4
Enter start state (format: Block On):
A B
B C
C D
D Table
Enter goal state (format: Block On):
D C
C B
B A
A Table
Enter depth limit: 3
Output:
Goal not found within depth limit.
How to Run
Prerequisites

Python 3.x
No external libraries required

Execution
bashpython block_world.py
Input Format
Block On
A Table    → Block A is on the table
B A        → Block B is on top of block A