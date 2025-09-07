Tic-Tac-Toe with Minimax Algorithm
Problem Statement
Tic-Tac-Toe (also known as Noughts and Crosses) is a two-player game played on a 3×3 grid. Players take turns marking spaces with their symbol:

Player (User): X
Computer (AI): O

The objective is to place three of your marks in a horizontal, vertical, or diagonal row before your opponent does.
This implementation uses the Minimax algorithm to create an unbeatable AI opponent that plays optimally.
Goal State
Winning Conditions:

Three X's or O's in a row (horizontal)
Three X's or O's in a column (vertical)
Three X's or O's in a diagonal

Game Outcomes:

User wins: Three X's aligned (+1 score)
Computer wins: Three O's aligned (-1 score)
Draw: Board full with no winner (0 score)

Objectives

Implement the Minimax algorithm for game tree search
Create an optimal AI player that never loses
Understand adversarial search in game theory
Apply recursive backtracking for decision-making
Demonstrate zero-sum game concepts

Algorithm: Minimax
Overview
Minimax is a decision-making algorithm used in two-player zero-sum games. It assumes:

Both players play optimally
One player (MAX) tries to maximize the score
The other player (MIN) tries to minimize the score

Core Concept
The algorithm explores the complete game tree:

Maximizing Player (User/X): Chooses moves that maximize the score
Minimizing Player (AI/O): Chooses moves that minimize the score

Evaluation Function
score = check_winner(board)

Returns:
  +1  → User (X) wins
  -1  → AI (O) wins
   0  → Draw or game in progress
Minimax Logic
From AI's perspective (Minimizer):

AI wants to minimize the score (achieve -1)
User wants to maximize the score (achieve +1)
AI assumes the user plays perfectly

Pseudocode
function minimax(board, is_ai_turn):
    score = check_winner(board)
    
    // Terminal states
    if score == +1 or score == -1:
        return score
    
    if board is full:
        return 0  // Draw
    
    if is_ai_turn (Minimizer):
        best_score = +∞
        for each empty position:
            place AI mark (O)
            score = minimax(board, False)
            undo move
            best_score = min(best_score, score)
        return best_score
    
    else (Maximizer):
        best_score = -∞
        for each empty position:
            place User mark (X)
            score = minimax(board, True)
            undo move
            best_score = max(best_score, score)
        return best_score
Finding Best Move
function find_best_move(board):
    best_value = +∞
    best_move = -1
    
    for each empty position i:
        place AI mark at position i
        move_value = minimax(board, False)  // User's turn next
        undo move
        
        if move_value < best_value:
            best_move = i
            best_value = move_value
    
    return best_move
Game Representation
Board Structure
Position indices:     Sample board:
 1 | 2 | 3             X | O | 3
---+---+---           ---+---+---
 4 | 5 | 6             4 | X | 6
---+---+---           ---+---+---
 7 | 8 | 9             O | 8 | 9

Internal representation: List of 9 elements [0-8]
User display: Numbered positions [1-9]
Empty cell: Space character ' '

Winning Patterns
8 possible winning combinations:
TypeIndicesDescriptionRow 1[0, 1, 2]Top horizontalRow 2[3, 4, 5]Middle horizontalRow 3[6, 7, 8]Bottom horizontalCol 1[0, 3, 6]Left verticalCol 2[1, 4, 7]Middle verticalCol 3[2, 5, 8]Right verticalDiag 1[0, 4, 8]Top-left to bottom-rightDiag 2[2, 4, 6]Top-right to bottom-left
Complexity Analysis
Time Complexity
Let:

b = branching factor (number of possible moves per state)
d = maximum depth of game tree

StageStatesBranching FactorNodesMove 19 emptyb = 99Move 28 emptyb = 872Move 37 emptyb = 7504............Complete tree~549,946
Worst Case Time Complexity: O(b^d) = O(9!)

For Tic-Tac-Toe: approximately 549,946 nodes
In practice: much fewer due to pruning from winning states

Space Complexity
O(d) = O(9)

Recursive call stack depth
Maximum 9 moves in Tic-Tac-Toe

Actual Performance
Due to early termination (winning states):

Average nodes explored: ~10,000–20,000
Response time: Near-instantaneous (<0.1s)

Sample Game Flow
Initial State
Board:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Enter your move (1-9): 5
After User Move
Board:
 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

Computer chooses position 1
After AI Move
Board:
 O | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9
Game Continues...
Enter your move (1-9): 3

Board:
 O | 2 | X
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

Computer chooses position 7

Board:
 O | 2 | X
---+---+---
 4 | X | 6
---+---+---
 O | 8 | 9
Example Outcomes
Computer Wins:
Board:
 O | X | X
---+---+---
 O | X | 6
---+---+---
 O | 8 | 9

Computer Wins!
Draw:
Board:
 X | O | X
---+---+---
 O | O | X
---+---+---
 X | X | O

It's a Draw!
How to Run
Prerequisites

Python 3.x
No external libraries required

Execution
bashpython tic_tac_toe.py
Sample Input/Output
Tic Tac Toe (User = X, Computer = O)

Board:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Enter your move (1-9): 5

Board:
 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

Computer chooses position 1

Board:
 O | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9

Enter your move (1-9): 9
...

Key Features
✅ Unbeatable AI: Uses optimal Minimax strategy
✅ Perfect Play: AI never loses (only wins or draws)
✅ Interactive: User-friendly command-line interface
✅ Input Validation: Handles invalid moves gracefully
✅ Complete Search: Explores entire game tree
✅ Efficient: Fast response time for 3×3 grid
Strategy Insights
Optimal First Moves
If AI plays first:

Corner (1, 3, 7, 9): Best opening move
Center (5): Second-best opening
Edge (2, 4, 6, 8): Weakest opening

AI Decision-Making
The AI:

Always blocks immediate user wins
Always takes immediate winning moves
Prefers center and corners
Forces draws when it cannot win
Never makes mistakes

Why the AI is Unbeatable
Game Theory Result:

Tic-Tac-Toe is a solved game
With perfect play from both sides → always a draw
Minimax guarantees perfect play → AI never loses

Best possible outcomes:

If user plays perfectly → Draw
If user makes mistakes → AI wins
User cannot win against perfect play