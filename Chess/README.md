Chess Game – Python Implementation
Overview

This project is a simple Python-based chess game implemented using basic programming constructs.
It focuses on representing a chessboard, validating moves for each piece, and updating the board after each move.

This version is designed for clarity rather than full competitive chess rules.

Features

✅ 8×8 chessboard represented using a 2D list
✅ Supports major chess pieces: king, queen, rook, bishop, knight, pawn
✅ Valid move checking for each piece
✅ Piece value scoring (pawn=1, knight=3, bishop=3, rook=5, queen=9)
✅ Turn-based move system
✅ Basic check for legal movement (no advanced rules)

How It Works

Board Initialization
The board is created as a matrix with lowercase letters for black pieces and uppercase for white pieces.

Move Validation
Each piece type has defined rules:

Pawn → forward movement and diagonal capture

Rook → straight lines

Bishop → diagonals

Knight → “L” shape

Queen → rook + bishop combined

King → one square in any direction

Executing Moves
After a move is validated:

The board updates

Captured pieces are removed

Scores update based on captured piece values

Game Loop