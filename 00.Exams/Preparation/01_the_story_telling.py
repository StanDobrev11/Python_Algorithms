command = input()

graph = {}
while command != 'End':
    command = command.split('->')
    node = command[0].strip()
    children = [] if not command[1] else command[1].split()
    graph[node] = children
    command = input()

visited = []
parent = []
# for key in graph:
#     parent[key] = None


def dfs(node, graph, visited, parent):
    if node in visited:
        return

    visited.append(node)
    for child in graph[node]:
        dfs(child, graph, visited, parent)
    parent.append(node)

for node in graph:
    dfs(node, graph, visited, parent)
parent.reverse()
print(*parent)
