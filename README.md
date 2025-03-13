# random_gen_keshav
Key Hyperparameters
MAX_INIT_TREE_DEPTH & MAX_ALLOWED_DEPTH:
These parameters define the maximum depth of the initial tree and the overall allowed tree depth. They control the complexity of the generated expressions.

POPULATION_SIZE:
The total number of alpha strategies (trees) to generate. For example, POPULATION_SIZE = 100000 creates one hundred thousand random alphas.

MAX_NODES:
A threshold used for bloat control. Trees that exceed this node count are pruned to keep the models simple and prevent overfitting.

Tree-Based Expression Generation
1. GPNode Class
Structure:
The GPNode class represents nodes in the expression tree. Nodes can be terminals (leaf nodes holding a value) or functions (unary, binary, or ternary) that combine or transform their children.

Methods:

to_expression(): Converts the tree into a mathematical expression.
count_nodes(): Recursively counts the nodes to enforce bloat control.
max_depth(): Computes the depth of the tree.
2. Random Tree Creation
The function generate_random_tree(max_depth, current_depth=1) recursively builds a random tree:

Terminal vs. Function Nodes:
At each recursive call, a random number determines whether a terminal node is created or whether the node will apply a unary, binary, or ternary transformation.

Random Choice of Functions and Parameters:
For non-terminal nodes, the function and, in some cases, an additional parameter (such as a window size or bucket expression) are chosen at random from predefined lists (e.g., UNARY_TRANSFORMS, BINARY_TRANSFORMS).

Bloat Control via Pruning:
The helper function prune_by_node_count ensures that the number of nodes in any generated tree does not exceed MAX_NODES. If a tree is too large, it is replaced by a simple terminal node.

3. Depth Enforcement
ensure_max_depth():
This function traverses the tree and replaces any branch exceeding the maximum allowed depth with a terminal node. This further guarantees that the final alpha expression remains within the defined complexity limits.
4. Iterative Node Collection
collect_nodes():
For scenarios where an iterable collection of all nodes is needed (e.g., for mutation or analysis), the collect_nodes function uses an iterative approach with a stack to gather nodes from the tree efficiently.
The Alpha Class
The Alpha class encapsulates the random alpha strategy:

Initialization:
If no tree is provided, the constructor generates a new random tree using the generate_random_tree function, applies depth enforcement, and then prunes it.

Sign & Expression Caching:
Each alpha has a sign attribute (to allow for contrarian adjustments) and caches its expression to avoid recomputation. If sign is -1, the expression is wrapped accordingly (e.g., with a function like math_multiply_negative_one).

Population Generation:
Finally, the code creates a large population of random alphas which are simulated(reversed) and submitted,
