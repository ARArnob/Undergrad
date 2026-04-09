A simple Python script to demonstrate and compare the Minimax and Alpha-Beta Pruning algorithms on a random binary game tree.

### Prerequisites

Make sure you have the following installed:

* `Python 3.x`

*(Note: The script uses only built-in modules `random` and `math`, so no additional pip packages are required.)*

### Installation

1. **Download the Script:**
   Save the Python code to a file, for example, `minimax_alphabeta.py`.

### Features

* Automatically generates a random binary game tree with 8 leaf nodes (values ranging from 2 to 25).
* Evaluates the tree using the standard Minimax algorithm.
* Evaluates the same tree using Alpha-Beta Pruning.
* Displays the total nodes evaluated by both algorithms, the nodes pruned, and the optimal value.
* Calculates the percentage of efficiency improvement achieved by Alpha-Beta Pruning.

### Usage

Run the script directly from your terminal. No input arguments are required as the leaf node values are generated randomly within the program.

```bash
python minimax_alphabeta.py
