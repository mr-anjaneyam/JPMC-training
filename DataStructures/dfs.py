def DFS(graph, start, visited = []):
    if len(visited) == 0:
        visited.append(start)
    for i in graph[start]:
        if i not in visited:
            visited.append(i)
            DFS(graph, i, visited)
    return visited
            

graph = {
    'A':['B', 'C'],
    'B':['A', 'C', 'D', 'E'],
    'C':['B', 'D'],
    'D':['B', 'C', 'E'],
    'E':['A', 'B', 'D']
}

out = DFS(graph, 'B')
print(out)