BFS and DFS Graph Profiling

Overview

This project demonstrates two fundamental graph traversal algorithms:

- Breadth First Search (BFS)
- Depth First Search (DFS)

Both algorithms are implemented on the same graph and profiled to compare their execution time and the number of nodes expanded while searching for a goal node.

Breadth First Search (BFS)

BFS explores a graph level by level.

It uses a queue (FIFO) to store nodes that need to be visited.

BFS Steps

1. Start from the source node.
2. Add the source node to the queue.
3. Remove a node from the front of the queue.
4. Visit its unvisited neighbouring nodes.
5. Add those neighbours to the queue.
6. Continue until the goal node is found or all reachable nodes are visited.

Depth First Search (DFS)

DFS explores a graph by going as deep as possible before backtracking.

It uses a stack (LIFO) or recursion.

DFS Steps

1. Start from the source node.
2. Visit the current node.
3. Move to an unvisited neighbouring node.
4. Continue deeper into the graph.
5. Backtrack when there are no unvisited neighbours.
6. Continue until the goal node is found or all reachable nodes are visited.

Graph Profiling

Graph profiling is used to measure the performance of BFS and DFS.

The following parameters are measured:

- Execution time
- Number of nodes expanded
- Minimum execution time
- Average execution time
- Maximum execution time

Python's "timeit" module can be used to measure execution time.

Py-spy can also be used to generate flame graphs showing where program execution time is spent.

BFS vs DFS

Feature| BFS| DFS
Data structure| Queue| Stack / Recursion
Traversal| Level by level| Depth first
Memory usage| Can be higher| Usually lower
Shortest path in unweighted graph| Yes| Not guaranteed
Main purpose| Level/shortest-path search| Deep exploration

Profiling Experiment

Both BFS and DFS are executed on the same graph and with the same starting node.

Different goal nodes can be selected to represent:

- Best-case search
- Average-case search
- Worst-case search

The execution times and node counts are recorded and compared.

Tools Used

- Python
- BFS
- DFS
- "timeit"
- Py-spy
- Graph data structure

Conclusion

BFS and DFS are important graph traversal techniques with different exploration strategies. Profiling helps compare their actual execution behaviour by measuring execution time and the number of nodes expanded on the same graph.
