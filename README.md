# Random Alpha Generation

This section details how random alpha strategies are generated using a genetic programming approach. Each alpha is represented as a tree structure that combines terminal values and functions (unary, binary, or ternary) to form a trading signal.

## Key Hyperparameters

- **MAX_INIT_TREE_DEPTH & MAX_ALLOWED_DEPTH:**  
  These parameters define the maximum depth of the initial tree and the overall allowed tree depth. They control the complexity of the generated expressions.

- **POPULATION_SIZE:**  
  The total number of alpha strategies (trees) to generate. For example, `POPULATION_SIZE = 100000` creates one hundred thousand random alphas.

- **MAX_NODES:**  
  A threshold used for bloat control. Trees that exceed this node count are pruned to keep the models simple and prevent overfitting.

## Tree-Based Expression Generation

### 1. GPNode Class

#### Structure:
- The `GPNode` class represents nodes in the expression tree.
- Nodes can be **terminals** (leaf nodes holding a value) or **functions** (nodes that apply unary, binary, or ternary operations to combine or transform their children).

#### Methods:
- **to_expression():** Converts the tree into a mathematical expression.
- **count_nodes():** Recursively counts the nodes to enforce bloat control.
- **max_depth():** Computes the depth of the tree.

### 2. Random Tree Creation

The function `generate_random_tree(max_depth, current_depth=1)` recursively builds a random tree:

- **Terminal vs. Function Nodes:**  
  At each recursive call, a random number determines whether to create a terminal node or a node that applies a unary, binary, or ternary transformation.

- **Random Choice of Functions and Parameters:**  
  For non-terminal nodes, the function (and sometimes an additional parameter such as a window size or bucket expression) is chosen at random from predefined lists (e.g., `UNARY_TRANSFORMS`, `BINARY_TRANSFORMS`).

- **Bloat Control via Pruning:**  
  The helper function `prune_by_node_count` ensures that the number of nodes in any generated tree does not exceed `MAX_NODES`. If the tree is too large, it is replaced by a simple terminal node.

### 3. Depth Enforcement

- **ensure_max_depth():**  
  This function traverses the tree and replaces any branch exceeding the maximum allowed depth with a terminal node. This ensures that the final alpha expression remains within the defined complexity limits.

### 4. Iterative Node Collection

- **collect_nodes():**  
  For scenarios where an iterable collection of all nodes is needed (e.g., for mutation or analysis), the `collect_nodes` function uses an iterative approach with a stack to efficiently gather nodes from the tree.

## The Alpha Class

The `Alpha` class encapsulates the random alpha strategy:

- **Initialization:**  
  If no tree is provided, the constructor generates a new random tree using the `generate_random_tree` function, applies depth enforcement with `ensure_max_depth()`, and then prunes it with `prune_by_node_count()`.

- **Sign & Expression Caching:**  
  Each alpha has a `sign` attribute (allowing for contrarian adjustments) and caches its expression to avoid recomputation. If `sign` is `-1`, the expression is wrapped accordingly (e.g., using a function like `math_multiply_negative_one`).

- **Population Generation:**  
  The code creates a large population of random alphas which can be simulated(reversed) and submitted.

