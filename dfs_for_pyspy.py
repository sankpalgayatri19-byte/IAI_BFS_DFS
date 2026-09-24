from dfs import dfs, graph

for _ in range(100000):
    dfs(graph, 'A', 'B')
    dfs(graph, 'A', 'I')
    dfs(graph, 'A', 'K')
