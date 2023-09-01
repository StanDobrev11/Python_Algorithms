from collections import deque

nodes = int(input())
edges = int(input())

graph = [[] for x in range(nodes + 1)]

for _ in range(edges):
    first, second = [int(x) for x in input().split()]
    graph[first].append(second)

start_node = int(input())
end_node = int(input())

visited = [False] * (nodes + 1)
parent = [None] * (nodes + 1)

queue = deque([start_node])
while queue:
    node = queue.popleft()
    if node == end_node:
        break
    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

path = []
node = end_node
while node is not None:
    path.insert(0, node)
    node = parent[node]
print(f'Shortest path length is: {len(path) - 1}')
print(*path)
