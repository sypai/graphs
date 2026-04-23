from collections import deque

def bfs(graph, source):
    if len(graph) == 0:
        return []
    
    q = deque([source])
    visited = set()
    result = []

    while q:
        node = q.pop()

        if node in visited:
            continue

        for neighbor in graph[node]:
            q.appendleft(neighbor)

        if not node in visited:
            result.append(node)
            visited.add(node)
    
    return result
