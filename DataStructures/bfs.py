def BFS(graph, start):
    queue = [start]
    visited = [start]
    while queue:
        temp = queue.pop(0)
        # print(temp, end=" ")
        for i in graph[temp]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return visited
            

graph = {
    'A':['B', 'C'],
    'B':['A', 'C', 'D', 'E'],
    'C':['B', 'D'],
    'D':['B', 'C', 'E'],
    'E':['A', 'B', 'D']
}

out = BFS(graph, 'D')
print(out)