from collections import deque

nodes = int(input())
pairs = int(input())

graph = {}
target_edges = []
max_node = -float('inf')
for _ in range(nodes):
    line = input().split(':')
    node = int(line[0])
    children = [int(x) for x in line[1].split()] if line[1] else []
    graph[node] = children
    max_node = max(node, max_node)
for _ in range(pairs):
    line = [int(x) for x in input().strip().split('-')]
    target_edges.append(line)



for start_node, end_node in target_edges:

    # visited = []
    visited = [False] * (max_node + 1)
    parent = [None] * (max_node + 1)

    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node == end_node:
            break
        # visited.append(node)
        visited[node] = True
        for child in graph[node]:
            # if child in visited:
            if visited[child]:
                continue
            # visited.append(child)
            visited[child] = True
            queue.append(child)
            parent[child] = node

    path = []
    node = end_node
    while node is not None:
        path.insert(0, node)
        node = parent[node]
    if len(path) == 1:
        print(f"{{{start_node}, {end_node}}} -> -1")
    else:
        print(f"{{{start_node}, {end_node}}} -> {len(path) - 1}")

