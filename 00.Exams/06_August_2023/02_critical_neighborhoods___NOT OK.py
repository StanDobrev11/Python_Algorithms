from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.weight = weight
        self.source = source
        self.destination = destination


streets = int(input())

street_list = []
town_list = {}

for _ in range(streets):
    source, destination, weight = [x for x in input().split(' - ')]
    street = Edge(source, destination, int(weight))
    # street_list.append(street)
    if source not in town_list:
        town_list[source] = []
    if destination not in town_list:
        town_list[destination] = []
    # town_list[source].append(destination)
    # town_list[destination].append(source)
    town_list[source].append(street)
    town_list[destination].append(street)

closed_roads = [x for x in input().split(',')]

start_city = input()
end_city = input()

distance = {}
source_track = {}  # parent
for key in town_list:
    source_track[key] = None
    distance[key] = float('inf')

distance[start_city] = 0

pq = PriorityQueue()
pq.put((0, start_city))  # distance, starting node
while not pq.empty():  # while have elements in the queue
    min_distance, node = pq.get()  # unpack the element in the queue
    if node == end_city:
        break
    for edge in town_list[node]:
        if f'{edge.source}-{edge.destination}' in closed_roads or f'{edge.destination}-{edge.source}' in closed_roads:
            continue
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            source_track[edge.destination] = node
            pq.put((new_distance, edge.destination))


path = deque()
node = end_city
while node is not None:
    path.appendleft(node)
    node = source_track[node]

print(*path, sep=' - ')
print(distance[end_city])
