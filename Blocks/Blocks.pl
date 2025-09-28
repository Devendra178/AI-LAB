% ------------------------------
% Block World Problem using Depth-Limited DFS
% ------------------------------

% ---------- State Equality ----------
same_state(State1, State2) :-
    msort(State1, Sorted1),
    msort(State2, Sorted2),
    Sorted1 = Sorted2.

% ---------- Check if a block is clear ----------
is_clear(Block, State) :-
    \+ member(on(_, Block), State).

% ---------- Replace a relation in the state ----------
replace_position(State, on(Block, Support), on(Block, NewSupport), NewState) :-
    select(on(Block, Support), State, on(Block, NewSupport), NewState).

% ---------- Generate possible moves ----------
make_move(State, NewState, move(Block, Target)) :-
    member(on(Block, Support), State),
    is_clear(Block, State),
    (
        % Move block to table
        Support \= table,
        replace_position(State, on(Block, Support), on(Block, table), NewState)
    ;
        % Move block onto another clear block
        member(on(Target, _), State),
        Block \= Target,
        is_clear(Target, State),
        replace_position(State, on(Block, Support), on(Block, Target), NewState)
    ).

% ---------- Depth-Limited DFS ----------
dfs(State, Goal, Path, _, Path) :-
    same_state(State, Goal).

dfs(State, Goal, Path, Depth, Solution) :-
    Depth > 0,
    make_move(State, NewState, Move),
    \+ member(NewState, Path),          % avoid cycles
    NewDepth is Depth - 1,
    dfs(NewState, Goal, [Move|Path], NewDepth, Solution).

% ---------- Solve Block World ----------
solve_blocks(Start, Goal, MaxDepth, Moves) :-
    dfs(Start, Goal, [], MaxDepth, RevMoves),
    reverse(RevMoves, Moves).

% ---------- Print the solution ----------
print_solution([]) :-
    writeln('No solution found.').

print_solution(Moves) :-
    writeln('SOLUTION FOUND:'),
    forall(member(move(Block, Target), Moves),
        (Target == table ->
            format('Move ~w to table~n', [Block]);
            format('Move ~w onto ~w~n', [Block, Target])
        )
    ).

% ---------- Example 1 ----------
example1 :-
    writeln('\nExample 1:'),
    writeln('Initial: B on A, A on table'),
    writeln('Goal: A on B, B on table\n'),
    Start = [on(a, table), on(b, a)],
    Goal  = [on(b, table), on(a, b)],
    ( solve_blocks(Start, Goal, 10, Moves) ->
        print_solution(Moves)
    ; writeln('No solution found.')
    ).

% ---------- Example 2 ----------
example2 :-
    writeln('\nExample 2:'),
    writeln('Initial: A, B, C all on table'),
    writeln('Goal: A on B, B on C, C on A (impossible circle)\n'),
    Start = [on(a, table), on(b, table), on(c, table)],
    Goal  = [on(a, b), on(b, c), on(c, a)],
    ( solve_blocks(Start, Goal, 10, Moves) ->
        print_solution(Moves)
    ; writeln('No solution found.')
    ).

% ---------- Run both examples ----------
run_examples :-
    example1,
    example2,
    writeln('\nProgram completed.').

% Run automatically
:- run_examples.
