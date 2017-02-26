# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The idea of naked twin problem solving algorithm is to identify 2 boxes in a unit with exactly one pair of common possible numbers, when we find such boxes we can therefore remove any of the number pair from the boxes peers. so by applying this constrain recursively we solve the problem (or make it easier).

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We apply a constraint to ensure that a number between 1-9 only appears only once in any given row, column or in a square unit, to solve diagonal sudoku problem we just have to apply the constrain to 2 diagonal units. By imply adding 2 new units (diagonal) to the "unit_list" constraint propagation happens automatically (as programmed ;))

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

