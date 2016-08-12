Structure of the input files:

(a) The Graph file: Simple adjacency matrix representation of the graph. An edge
    between 2 vertices is represented as a 1 in the matrix, and 0 otherwise.

    Example (undirected) graph with 3 vertices and edges [[0, 1], [1, 2]]:

    0 1 0
    1 0 1
    0 1 0

(b) The Vertex Weights file: The algorithm works with vertex-weighted graphs, so
    the weights of the vertices are represented in this file (in order).

    Example of the above graph with vertex weights {(0, 5), (1, 3), (2, 8)}:

    5
    3
    8
