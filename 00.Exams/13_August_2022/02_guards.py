nodes = int(input())
edges_count = int(input())

graph = {}
for _ in range(edges_count):
    first, second = [int(x) for x in input().split()]
    if first not in graph:
        graph[first] = []
    graph[first].append(second)
    if second not in graph:
        graph[second] = []

starting_node = int(input())

# print(graph)

visited = set()


def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)


dfs(starting_node, graph, visited)

# not_visited = []
for node in sorted(graph):
    if node not in visited:
        # not_visited.append(node)
        print(node, end=' ')
