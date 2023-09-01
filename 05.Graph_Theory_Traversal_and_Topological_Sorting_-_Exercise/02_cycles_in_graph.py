def find_children_count(graph):
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


def find_zero_parent(children_count):
    for node in children_count:
        if children_count[node] == 0:
            return node
    return None


graph = {}

command = input()
while not command == 'End':
    line = command.split('-')
    node = line[0]
    children = line[1]
    graph[node] = children

    command = input()

children_count = find_children_count(graph)
# print(children_count)

is_cyclic = False
while children_count:
    node_zero = find_zero_parent(children_count)
    if node_zero is None:
        is_cyclic = True
        break
    children_count.pop(node_zero)
    for node, value in graph.items():
        if node == node_zero:
            children_count[value] -= 1

if is_cyclic:
    print("Acyclic: No")
else:
    print("Acyclic: Yes")
