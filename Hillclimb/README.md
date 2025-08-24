# 8-Puzzle Problem using Hill Climbing (C++)

This project implements a *basic Hill Climbing algorithm* to solve the *8-Puzzle problem* using C++. 

##  Problem Description

The *8-Puzzle* consists of a 3×3 grid containing tiles numbered 1–8 and one empty space (0).  
A move is performed by sliding a tile into the empty space.

The goal is to reach the final configuration:

1 2 3
4 5 6
7 8 0


---

## Algorithm Used: Hill Climbing

Hill Climbing is a local search algorithm that:

1. Starts from an initial state  
2. Evaluates its *heuristic* (cost)  
3. Generates all possible next states  
4. Moves to the neighbor with the *lowest heuristic*  
5. Stops when:
   - The goal state is reached  
   - No neighbor is better (local optimum)

---

##  Heuristic Function

This implementation uses the *Misplaced Tiles Heuristic (Hamming Distance)*:

> Count how many tiles are not in their correct position.

Example:
- If 3 tiles are misplaced, heuristic = 3

This helps guide the search toward the goal.

---

##  Features of This Implementation

- Simple and minimal code  
- No classes, only functions  
- Prints each step taken  
- Detects local optimum (when stuck)  
- Uses 0 as the blank tile  
- Easy to understand and modify  

---

Example Output-

Start State:
1 2 3
4 0 6
7 5 8
--------
Move with heuristic: 2
...
Reached Goal!