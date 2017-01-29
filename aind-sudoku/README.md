# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: In naked twin problem if two boxes are in a same unit(row/column/diagonal/square) and have same values of length 2 then these two states are confined to only these two boxes and the rest of the peers in the same unit can't have them as solved values.This is the constraint used in the reduction of puzzle for naked twin problem.

For naked twins problem we consider only those boxes with values of the box which have length 2, i.e, two possible search states.Then we find if the values[box] has a twin box, i.e, box with same value. If there is a twin box then we identify which unit do they both belong to (row/column/square/diagonal) and remove this values[box] from all the other peers in the same unit. 

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We check all the constraints such as elimination and only_option for all the elements in both the diagonals of the sudoku.We can also apply naked twin to the same.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
