def find_child_count(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0

        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1

    return result


def find_zero_nodes(count):
    for node in count:
        if count[node] == 0:
            return node

    return None


nodes = int(input())

graph = {}
for _ in range(nodes):
    line = input().split('->')
    node = line[0].strip()
    child = line[1].strip().split(', ') if line[1] else []
    graph[node] = child

# print(graph)

nodes_count = find_child_count(graph)
# print(nodes_count)
sorted = []
has_cycle = False
while nodes_count:
    zero_node = find_zero_nodes(nodes_count)
    if zero_node is None:
        has_cycle = True
        break

    sorted.append(zero_node)
    nodes_count.pop(zero_node)
    for child in graph[zero_node]:
        nodes_count[child] -= 1

if has_cycle:
    print('Invalid topological sorting')
else:
    print(f"Topological sorting: {', '.join(sorted)}")