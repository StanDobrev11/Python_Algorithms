from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.weight = weight
        self.source = source
        self.destination = destination
    def __gt__(self, other):
        return self.weight > other.weight

edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [x for x in input().split(' - ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, int(weight)))
    graph[destination].append(Edge(destination, source, int(weight)))

closed_edges = [x for x in input().split(',')]

start_node = input()
target_node = input()

distance = {}
parent = {}
for key in graph:
    parent[key] = None
    distance[key] = float('inf')

distance[start_node] = 0
visited = set()
pq = PriorityQueue()
pq.put((0, start_node))
while not pq.empty():
    min_distance, node = pq.get()

    if node == target_node:
        break
    for edge in graph[node]:
        # if f"{edge.source}-{edge.destination}" in visited:
        #     continue
        # visited.add(f"{edge.source}-{edge.destination}")
        if f'{edge.source}-{edge.destination}' in closed_edges or f'{edge.destination}-{edge.source}' in closed_edges:
            continue
        closed_edges.append(f"{edge.source}-{edge.destination}")
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            pq.put((new_distance, edge.destination))

path = deque()
node = target_node
while node is not None:
    path.appendleft(node)
    node = parent[node]

print(*path, sep=' - ')
print(distance[target_node])
