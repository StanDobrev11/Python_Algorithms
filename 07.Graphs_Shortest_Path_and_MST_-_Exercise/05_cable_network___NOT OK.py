from queue import PriorityQueue


def prim(forest, forest_edges, non_forest_edges, cost, budget):
    cost = 0
    pq = PriorityQueue()
    for edge in sorted(non_forest_edges, key=lambda x: x.weight):
        pq.put(edge)
    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = None

        if min_edge.source in forest and min_edge.destination not in forest:
            non_tree_node = min_edge.destination
        elif min_edge.destination in forest and min_edge.source not in forest:
            non_tree_node = min_edge.source

        if non_tree_node is None:
            continue

        forest.add(non_tree_node)
        forest_edges.append(min_edge)
        cost += min_edge.weight
        if cost > budget:
            cost -= min_edge.weight
            break

    return cost


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


budget = int(input())
nodes = int(input())
edges = int(input())

graph = {}
forest = set()
forest_edges = []
non_forest_edges = []
cost = 0

for _ in range(edges):
    line = input().split()
    source, destination, weight, = int(line[0]), int(line[1]), int(line[2])
    edge = Edge(source, destination, weight)

    if len(line) > 3:
        forest.add(source)
        forest.add(destination)
        forest_edges.append(edge)
    else:
        non_forest_edges.append(edge)

cost = prim(forest, forest_edges, non_forest_edges, cost, budget)

print(f'Budget used: {cost}')
