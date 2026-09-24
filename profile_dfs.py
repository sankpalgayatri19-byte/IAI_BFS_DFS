import timeit
from dfs import dfs, graph


def measure(goal):
    times = []

    for i in range(10):
        time_taken = timeit.timeit(
            lambda: dfs(graph, 'A', goal),
            number=1
        )

        times.append(time_taken * 1000)

    best = min(times)
    average = sum(times) / len(times)
    worst = max(times)

    nodes = dfs(graph, 'A', goal)

    return best, average, worst, nodes


print("================================")
print("       DFS PROFILING RESULTS")
print("================================")

# Best case
best = measure('B')

print("\nBEST CASE")
print("Goal: B")
print("Best Time    : {:.6f} ms".format(best[0]))
print("Average Time : {:.6f} ms".format(best[1]))
print("Worst Time   : {:.6f} ms".format(best[2]))
print("Nodes        :", best[3])


# Average case
average = measure('I')

print("\nAVERAGE CASE")
print("Goal: I")
print("Best Time    : {:.6f} ms".format(average[0]))
print("Average Time : {:.6f} ms".format(average[1]))
print("Worst Time   : {:.6f} ms".format(average[2]))
print("Nodes        :", average[3])


# Worst case
worst = measure('K')

print("\nWORST CASE")
print("Goal: K")
print("Best Time    : {:.6f} ms".format(worst[0]))
print("Average Time : {:.6f} ms".format(worst[1]))
print("Worst Time   : {:.6f} ms".format(worst[2]))
print("Nodes        :", worst[3])
