def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)


def path_exists(source, destination, graph):
    visited = set()

    dfs(source, graph, visited)

    return destination in visited


nodes = int(input())
graph = {}
for _ in range(nodes):
    line = input().split(' -> ')
    node = line[0]
    child = line[1].split()
    graph[node] = child

# print(graph)
edges = []
for node in graph:
    for child in graph[node]:
        edges.append((node, child))

removed_edges = []
for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, graph):
        removed_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(removed_edges)}')
for first, second in removed_edges:
    print(f'{first} - {second}')

