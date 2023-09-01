def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


class Edge:
    def __init__(self, source, destination, weight):
        self.weight = weight
        self.source = source
        self.destination = destination


towns = int(input())    # nodes
streets = int(input()) # edges

street_list = []    # graph

for _ in range(streets):
    source, destination, weight = [int(x) for x in input().split(' - ')]
    street = Edge(source, destination, weight)
    street_list.append(street)
source_track = [num for num in range(towns)] # parent

connected = [] # forest

for street in sorted(street_list, key=lambda s: s.weight):
    source_town_root = find_root(source_track, street.source)
    destination_town_root = find_root(source_track, street.destination)
    if source_town_root != destination_town_root:
        source_track[source_town_root] = destination_town_root
        connected.append(street.weight)

print(f'Total cost: {sum(connected)}')
