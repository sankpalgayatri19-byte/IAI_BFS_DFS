from collections import deque


def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    nodes_expanded = 0

    while queue:
        node = queue.popleft()
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return nodes_expanded


# Graph
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


print("========== BFS ==========")

# Best case
nodes = bfs(graph, 'A', 'B')
print("Best Case - Goal: B")
print("Nodes Expanded:", nodes)

# Average case
nodes = bfs(graph, 'A', 'I')
print("\nAverage Case - Goal: I")
print("Nodes Expanded:", nodes)

# Worst case
nodes = bfs(graph, 'A', 'K')
print("\nWorst Case - Goal: K")
print("Nodes Expanded:", nodes)
