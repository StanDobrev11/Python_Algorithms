def dfs(node, graph, visited, connected):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, connected)
    connected.append(node)


number_of_nodes = int(input())

graph = []

for node in range(number_of_nodes):
    graph.append([int(x) for x in input().split()])

visited = [False] * number_of_nodes
connected = []

for node in range(len(graph)):
    dfs(node, graph, visited, connected)
    if len(connected) > 0:
        print(f'Connected component: {" ".join([str(x) for x in connected])}')
    connected.clear()
