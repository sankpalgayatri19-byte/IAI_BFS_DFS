def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        # Reverse order to make traversal predictable
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return nodes_expanded


# Same graph used for fair comparison
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}


print("========== DFS ==========")

# Best case
nodes = dfs(graph, 'A', 'B')
print("Best Case - Goal: B")
print("Nodes Expanded:", nodes)

# Average case
nodes = dfs(graph, 'A', 'I')
print("\nAverage Case - Goal: I")
print("Nodes Expanded:", nodes)

# Worst case
nodes = dfs(graph, 'A', 'K')
print("\nWorst Case - Goal: K")
print("Nodes Expanded:", nodes)
