class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


num_edges = int(input())

graph = []
parent = []
max_node = -float("inf")

for _ in range(num_edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node)
    # if first not in parent:
    #     parent.append(first)
    # if second not in parent:
    #     parent.append(second)

parent = [num for num in range(max_node + 1)]
# parent.sort()
forest = []
for edge in sorted(graph, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.first)
    second_nood_root = find_root(parent, edge.second)
    if first_node_root != second_nood_root:
        parent[first_node_root] = second_nood_root
        forest.append(edge)

for edge in forest:
    print(f"{edge.first} - {edge.second}")
