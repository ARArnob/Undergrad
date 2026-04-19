## A collection of Python scripts demonstrating foundational Artificial Intelligence algorithms and basic programming logic, completed as part of a lab final examination.

### Prerequisites

Make sure you have the following installed:

* `Python 3.x`

*(Note: The scripts use only built-in modules, so no additional pip packages are required.)*

### Installation

1. **Download the Repository:**
   Clone or download the folder containing the scripts to your local machine.

### Features

The repository contains four distinct problem-solving scripts:

* **Question 1 (Number Checker):** A conditional logic script that evaluates user input to determine if a number is positive, negative, or zero, and independently checks if its absolute value is even or odd.
* **Question 2 (Depth-First Search):** Implements a DFS pathfinding algorithm on a predefined 5x5 binary grid. It traverses available paths, calculates the total number of reachable cells from a starting coordinate, and tracks the exact traversal history.
* **Question 3 (Graph Coloring):** Solves a constraint satisfaction problem using backtracking. It takes a user-defined set of edges and finds the minimum number of colors required to color a 6-node graph so that no two connected nodes share the same color.
* **Question 4 (Alpha-Beta Pruning):** Evaluates a static binary game tree with 8 leaf nodes using the Alpha-Beta Pruning algorithm. It outputs the optimal value, the total number of nodes evaluated, and the total number of branches successfully pruned.

### Usage

Run the scripts directly from your terminal. 

```bash
python problem_01.py
python problem_02.py
python problem_03.py
python problem_04.py
```

*(Note: `question1.py` and `question3.py` require you to manually input data into the terminal when prompted. `question2.py` and `question4.py` execute automatically using internal base values.)*
