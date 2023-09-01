from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))
    graph[destination].append(Edge(destination, source, weight))

start_node = int(input())
end_node = int(input())

reliability = [float('-inf')] * nodes
reliability[start_node] = 100
parent = [None] * nodes

pq = PriorityQueue()
pq.put((100, start_node))
while not pq.empty():
    max_reliability, node = pq.get()
    if node == end_node:
        break
    for edge in graph[node]:
        # because we have undirected graph in order to cover all nodes without doubling
        child = edge.source if edge.destination == node else edge.destination
        new_reliability = abs(max_reliability * edge.weight / 100)
        if new_reliability > reliability[child]:
            reliability[child] = new_reliability
            parent[child] = node
            # in order to get max number instead of min, add to queue negative number
            # and work with negatves:
            # 53, 65, 76 - next in line is 53
            # however -53, -65, -76 - next in line is -76 that is why we use abs()
            pq.put((-new_reliability, child))

path = deque()
node = end_node
while node is not None:
    path.appendleft(node)
    node = parent[node]

print(f'Most reliable path reliability: {reliability[end_node]:.2f}%')
print(*path, sep=' -> ')



