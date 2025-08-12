# Tic Tac Toe using Minimax Algorithm

## Aim
To implement the Tic Tac Toe game in C++ where a human player competes against an AI opponent that uses the *Minimax Algorithm* based on *Game Theory* to always play optimally.

---

## Theory

### Game Theory
Game Theory is the study of decision-making in competitive situations where multiple players interact.  
In *Tic Tac Toe*, two players (Human and AI) take alternate turns, and the game is deterministic (no chance events).  
Optimal strategies ensure the best possible outcome regardless of the opponent’s moves.

### Minimax Algorithm
The *Minimax Algorithm* is a recursive decision-making algorithm used for two-player games:
- *Maximizer (AI)*: Tries to maximize its score (winning).  
- *Minimizer (Human)*: Tries to minimize AI’s score (forcing AI to lose or draw).  

The evaluation:
- *+10* → AI wins  
- *-10* → Human wins  
- *0* → Draw  

At each step:
1. AI simulates all possible moves.  
2. Human simulates all possible counter-moves.  
3. Backtracking propagates the best move upwards.  
4. AI selects the move that *maximizes its chance of winning*.  

This ensures that the AI *never loses* (at worst, it draws).

---

## Data Representation
- *Board:* A 3×3 matrix (char board[3][3]) with values:
  - 'X' → Human move  
  - 'O' → AI move  
  - ' ' → Empty cell  

- *Player Representation:*
  - Human → PLAYER = 1  
  - AI → AI = 2  

- *Functions Used:*
  - initBoard() → Initialize empty board  
  - printBoard() → Display current board state  
  - checkWin() → Check winner (PLAYER, AI, or none)  
  - movesLeft() → Check if moves remain  
  - minimax() → Core recursive algorithm  
  - bestMove() → Select optimal AI move  

---

## Methodology
1. Initialize the empty board.  
2. Human enters their move (X).  
3. AI calculates the *best possible move* using minimax().  
4. Game continues until:
   - Human wins (-10)  
   - AI wins (+10)  
   - No moves left → Draw  

---

## Time Complexity
- *Minimax explores the entire game tree.*  
- Total possible board states in Tic Tac Toe = *9! = 362,880*.  
- In practice, due to pruning (invalid/won states), the explored states are fewer.  

*Time Complexity:*  
- Worst Case: O(b^d)  
  - b = Branching factor (up to 9 moves)  
  - d = Depth of the tree (9 moves maximum)  
- For Tic Tac Toe: *O(9!) ≈ 362,880 evaluations* (still manageable).  

---

## Space Complexity
- The recursion stack depth can go up to *9* (maximum moves).  
- Additional memory for storing states is negligible.  

*Space Complexity:* O(d) = O(9) ≈ constant.  

---

## Conclusion
The *Minimax Algorithm with Game Theory* ensures the AI plays optimally.  
- The AI *never loses* — it either wins or forces a draw.  
- Demonstrates the power of *adversarial search* in decision-making.  

This implementation is a fundamental example of applying *AI search strategies* in games.