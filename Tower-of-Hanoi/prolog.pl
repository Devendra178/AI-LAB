% ---------- Tower of Hanoi in Prolog ----------
% Move N disks from Source to Target using Auxiliary

move(1, Source, Target, _) :-
    format('Move disk 1 from ~w → ~w~n', [Source, Target]).

move(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    move(M, Source, Auxiliary, Target),
    format('Move disk ~w from ~w → ~w~n', [N, Source, Target]),
    move(M, Auxiliary, Target, Source).

hanoi(N) :-
    N >= 3,
    format('Number of disks: ~w~n', [N]),
    Moves is (2 ** N) - 1,
    format('Minimum moves required: ~w~n~n', [Moves]),
    move(N, 'A', 'C', 'B'),
    write('🎯 Puzzle solved!'), nl.

run :-
    write('🏰 Tower of Hanoi in Prolog 🧠'), nl,
    write('Enter number of disks (minimum 3): '),
    read(N),
    ( N >= 3 ->
        hanoi(N)
    ;   write('Please enter at least 3 disks.'), nl
    ).

:- initialization(run).
