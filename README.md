# Sudoku

# How do we apply constraint propagation to solve the naked twins problem?

In naked twin problem if two boxes are in a same unit(row/column/diagonal/square) and have same values of length 2 then these two states are confined to only these two boxes and the rest of the peers in the same unit can't have them as solved values.This is the constraint used in the reduction of puzzle for naked twin problem.

For naked twins problem we consider only those boxes with values of the box which have length 2, i.e, two possible search states.Then we find if the values[box] has a twin box, i.e, box with same value. If there is a twin box then we identify which unit do they both belong to (row/column/square/diagonal) and remove this values[box] from all the other peers in the same unit. 

# How do we apply constraint propagation to solve the diagonal sudoku problem?

We check all the constraints such as elimination and only_option for all the elements in both the diagonals of the sudoku.We can also apply naked twin to the same.
