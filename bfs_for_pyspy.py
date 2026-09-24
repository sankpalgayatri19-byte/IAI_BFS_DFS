from bfs import bfs, graph

for _ in range(100000):
    bfs(graph, 'A', 'B')
    bfs(graph, 'A', 'I')
    bfs(graph, 'A', 'K')
